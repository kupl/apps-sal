class Solution:

    def validateBinaryTreeNodes(self, n: int, l: List[int], r: List[int]) -> bool:
        s = set()
        d = [0] * n
        for i in l:
            if i != -1:
                d[i] = 1
        for i in r:
            if i != -1:
                d[i] = 1
        q = []
        for i in range(n):
            if not d[i]:
                q.append(i)
                break
        if len(q) == 0:
            return False
        while len(q):
            t = q.pop()
            s.add(t)
            if l[t] in s or r[t] in s:
                return False
            if l[t] != -1:
                q.append(l[t])
            if r[t] != -1:
                q.append(r[t])
        if len(s) == n:
            return True
        else:
            return False
