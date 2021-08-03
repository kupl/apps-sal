class Solution:
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

        visited = set([A])
        queue = collections.deque([A])

        k = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                for nbor in getNeighbors(word):
                    if nbor not in visited:
                        if nbor == B:
                            return k
                        queue.append(nbor)

            k += 1

        raise Exception('invalid')
