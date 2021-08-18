class Solution:
    def kSimilarity(self, A: str, B: str) -> int:

        def dist(a, b):
            return sum((1 if c != d else 0 for (c, d) in zip(a, b)))

        def find_wrong_letters(working):
            wants = defaultdict(set)
            wrongs = defaultdict(set)
            for i, c in enumerate(working):
                target = A[i]
                if c != target:
                    wants[target].add(i)
                    wrongs[c].add(i)
            return wants, wrongs

        def swap(s, i, j):
            if i > j:
                i, j = j, i
            return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

        def extend(working):
            wrongs, needs = find_wrong_letters(working)
            for letter, wrong_set in list(wrongs.items()):
                return (swap(working, i, j) for i in wrong_set for j in needs[letter])

        q = deque()
        q.append((0, 0, B))
        seen = dict()
        best = len(A)
        while q:
            estimate, k, working = q.popleft()
            if estimate >= best or k >= best:
                return best
            if working == A:
                best = min(best, k)
                continue

            improves_one, improves_two = [], []
            for extension in extend(working):
                improvement = dist(A, working) - dist(A, extension)
                if improvement == 2:
                    improves_two.append(extension)
                else:
                    improves_one.append(extension)
            for extension in improves_two or improves_one:
                if extension not in seen or seen[extension] > k + 1:
                    seen[extension] = k + 1
                    q.append((0, k + 1, extension))
        return best
