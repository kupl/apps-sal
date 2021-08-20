class Solution:

    def kSimilarity(self, A: str, B: str) -> int:

        def next(s):
            for i in range(len(s)):
                if s[i] != B[i]:
                    for j in range(i + 1, len(s)):
                        if B[i] == s[j] and B[j] == s[i]:
                            yield (s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:])
                    for j in range(i + 1, len(s)):
                        if B[i] == s[j] and B[j] != s[j]:
                            yield (s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:])
                    return
        res = 0
        if A == B:
            return res
        q = [(A, 0)]
        seen = {A}
        for (s, i) in q:
            if s == B:
                return i
            for n in next(s):
                if n not in seen:
                    q.append((n, i + 1))
                    seen.add(n)
        return -1
