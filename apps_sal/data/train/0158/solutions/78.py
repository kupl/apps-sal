class Solution:
    def kSimilarity2(self, A, B):
        def nei(x):
            i = 0
            while x[i] == B[i]:
                i += 1
            for j in range(i + 1, len(x)):
                if x[j] == B[i] and x[i] != x[j]:
                    yield x[:i] + x[j] + x[i + 1:j] + x[i] + x[j + 1:]

        q, seen = collections.deque([(A, 0)]), {A}
        while q:
            x, d = q.popleft()
            if x == B:
                return d
            for y in nei(x):
                if y not in seen:
                    seen.add(y), q.append((y, d + 1))

    def kSimilarity(self, A: str, B: str) -> int:
        if A == B:
            return 0

        m = len(A)

        def getNeighbors(word):
            i = 0
            while word[i] == B[i]:
                i += 1

            for j in range(i + 1, m):
                if word[j] == B[i] and word[j] != word[i]:
                    yield word[:i] + word[j] + word[i + 1:j] + word[i] + word[j + 1:]

        visited = {A}
        queue = collections.deque([(A, 0)])

        while queue:
            word, d = queue.popleft()
            if word == B:
                return d
            for nbor in getNeighbors(word):
                if nbor not in visited:
                    visited.add(nbor)
                    queue.append((nbor, d + 1))
