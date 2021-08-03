from collections import deque


class Solution:
    def kSimilarity(self, A: str, B: str) -> int:

        def nei(x):
            i = 0
            while x[i] == B[i]:
                i += 1
            for j in range(i + 1, len(x)):
                if x[j] == B[i] and x[j] != B[j]:
                    yield x[:i] + x[j] + x[i + 1:j] + x[i] + x[j + 1:]

        if not A or not B:
            return 0

        queue, visited = [(A, 0)], {A}

        for x, d in queue:
            if x == B:
                return d
            for y in nei(x):
                if y not in visited:
                    visited.add(y)
                    queue.append((y, d + 1))
