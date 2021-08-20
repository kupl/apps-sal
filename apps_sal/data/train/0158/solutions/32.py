class Solution:

    def kSimilarity(self, A: str, B: str) -> int:

        def neighbor(x):
            i = 0
            while x[i] == B[i]:
                i += 1
            for j in range(i + 1, len(x)):
                if x[j] == B[i] and x[j] != B[j]:
                    yield (x[:i] + x[j] + x[i + 1:j] + x[i] + x[j + 1:])
        (queue, seen) = ([(A, 0)], {A})
        for (word, distance) in queue:
            if word == B:
                return distance
            for neigh in neighbor(word):
                if neighbor not in seen:
                    seen.add(neigh)
                    queue.append((neigh, distance + 1))
