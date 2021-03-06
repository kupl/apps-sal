class Solution:

    def kSimilarity(self, A: str, B: str) -> int:

        def find(s):
            i = 0
            res = []
            while s[i] == B[i]:
                i += 1
            for j in range(i + 1, len(B)):
                if s[j] == B[i]:
                    res.append(s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:])
            return res
        q = collections.deque([[0, A]])
        seen = set([A])
        while q:
            size = len(q)
            for _ in range(size):
                (step, s) = q.popleft()
                if s == B:
                    return step
                for new in find(s):
                    if new not in seen:
                        seen.add(new)
                        q.append([step + 1, new])
        return
