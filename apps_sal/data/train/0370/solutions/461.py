class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        A = set(A)
        n = max(A) + 1
        p = [True] * n
        p[0] = p[1] = False
        (dic1, dic2) = (collections.defaultdict(set), collections.defaultdict(set))
        for i in range(2, n):
            if p[i]:
                if i in A:
                    dic1[i].add(i)
                    dic2[i].add(i)
                for j in range(i * 2, n, i):
                    p[j] = False
                    if j in A:
                        dic1[i].add(j)
                        dic2[j].add(i)
        seen = set()
        res = 0
        for num in A:
            if num not in seen:
                seen.add(num)
                (cur, s) = (0, [num])
                while s:
                    node = s.pop()
                    cur += 1
                    for m in dic2[node]:
                        for nxt in dic1[m]:
                            if nxt not in seen:
                                seen.add(nxt)
                                s.append(nxt)
                        dic1.pop(m)
                res = max(res, cur)
        return res
