class Solution:

    def kSimilarity(self, A: str, B: str) -> int:

        def dist(a, b):
            return sum((1 if c != d else 0 for (c, d) in zip(a, b)))

        def find_wrong_letters(working):
            wants = defaultdict(set)
            wrongs = defaultdict(set)
            for (i, c) in enumerate(working):
                target = A[i]
                if c != target:
                    wants[target].add(i)
                    wrongs[c].add(i)
            return (wants, wrongs)

        def estimate_remaining(string):
            count = dist(string, A)
            return count / 2 if count % 2 == 0 else count // 2 + 1

        def swap(s, i, j):
            if i > j:
                (i, j) = (j, i)
            return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

        def extend(working):
            (wrongs, needs) = find_wrong_letters(working)
            for (letter, wrong_set) in list(wrongs.items()):
                return (swap(working, i, j) for i in wrong_set for j in needs[letter])
        if A == B:
            return 0
        q = [(0, 0, B)]
        seen = dict()
        best = len(A)
        while q:
            (estimate, k, working) = heapq.heappop(q)
            if estimate >= best or k >= best:
                return best
            if working == A:
                best = min(best, k)
                continue
            for extension in extend(working):
                if extension not in seen or seen[extension] > k + 1:
                    seen[extension] = k + 1
                    new_estimate = estimate_remaining(extension) + k + 1
                    heapq.heappush(q, (new_estimate, k + 1, extension))
        return best
