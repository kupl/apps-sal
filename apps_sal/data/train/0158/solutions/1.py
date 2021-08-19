class Solution:

    def kSimilarity(self, A: str, B: str) -> int:
        if A == B:
            return 0

        def neighbors(s, i=0):
            while s[i] == B[i]:
                i += 1
            for j in range(i + 1, len(A)):
                if s[j] == B[i] and B[j] == s[i]:
                    yield (s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:])
                    return
            for j in range(i + 1, len(A)):
                if s[j] == B[i] and s[j] != B[j]:
                    yield (s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:])
        dp = collections.deque([(A, 0)])
        met = set()
        while dp:
            (A_, step) = dp.popleft()
            for n in neighbors(A_):
                if n == B:
                    return step + 1
                if n not in met:
                    dp.append((n, step + 1))
                    met.add(n)
