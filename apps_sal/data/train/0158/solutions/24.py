class Solution:
    def kSimilarity(self, A: str, B: str) -> int:

        def dist(a, b):
            return sum((1 if c != d else 0 for (c, d) in zip(a, b)))

        def swap(s, i, j):
            if i > j:
                i, j = j, i
            return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

        def DFS(string, k):
            if string == A:
                return True
            if k == 0:
                return False
            for i, c in enumerate(string):
                if A[i] == c:
                    continue
                for j in range(i, len(A)):
                    if string[j] == A[i] and A[j] != A[i]:
                        if DFS(swap(string, i, j), k - 1):
                            return True
                return False

        for k in range(len(A)):
            if DFS(B, k):
                return k
