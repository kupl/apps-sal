class Solution:
    def findLatestStep(self, A: List[int], m: int) -> int:
        n = len(A)
        if m == n:
            return n
        dic = {0: [0, 0]}

        def union(a, b):
            fa = find(a)
            fb = find(b)
            if fa != fb:
                dic[fa[0]] = [fb[0], fa[1] + fb[1]]
                dic[fb[0]] = dic[fa[0]]
                dic[a] = dic[fa[0]]
                dic[b] = dic[fa[0]]

        def find(a):
            if dic[a][0] != a:
                dic[a] = find(dic[a][0])
            return dic[a]

        ans, t, ret = set(), 0, -1
        for i, v in enumerate(A):
            t = t | (1 << (v - 1))
            dic[v] = [v, 1]
            if v - 1 in dic:
                if find(v - 1)[1] == m:
                    ans.remove(dic[v - 1][0])
                union(v, v - 1)
            if v + 1 in dic:
                if find(v + 1)[1] == m:
                    ans.remove(dic[v + 1][0])
                union(v, v + 1)
            if dic[v][1] == m:
                ans.add(dic[v][0])
            if ans:
                ret = i + 1
        return ret
