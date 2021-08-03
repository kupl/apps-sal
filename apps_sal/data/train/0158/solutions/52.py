class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        if A == B:
            return 0
        visited = set([A])
        q = collections.deque([A])
        res, n = 0, len(A)
        while q:
            res += 1
            qn = len(q)
            for _ in range(qn):
                s = q.popleft()
                i = 0
                while i < n and s[i] == B[i]:
                    i += 1
                for j in range(i + 1, n):
                    if s[j] == B[j] or s[j] != B[i]:
                        continue
                    tmp = self.swap(s, i, j)
                    if tmp == B:
                        return res
                    if tmp not in visited:
                        visited.add(tmp)
                        q.append(tmp)
        return res

    def swap(self, s: str, i: int, j: int) -> str:
        l = list(s)
        l[i], l[j] = l[j], l[i]
        return ''.join(l)
