class Solution:

    def findLatestStep(self, a: List[int], m: int) -> int:
        n = len(a)
        a = [i - 1 for i in a]
        val = [[i, i] for i in range(n)]
        par = [i for i in range(n)]
        lis = [0] * n

        def find(chi):
            if par[chi] == chi:
                return chi
            temp = find(par[chi])
            par[chi] = temp
            return temp

        def union(i, j):
            pari = find(i)
            parj = find(j)
            par[parj] = pari
            val[pari][0] = min(val[parj][0], val[pari][0])
            val[pari][1] = max(val[parj][1], val[pari][1])
        ans = -1
        cnt = 0
        for i in range(len(a)):
            lis[a[i]] = 1
            if a[i] - 1 >= 0 and lis[a[i] - 1] == 1:
                tval = val[find(a[i] - 1)]
                if tval[1] - tval[0] + 1 == m:
                    cnt -= 1
                union(a[i] - 1, a[i])
            if a[i] + 1 < n and lis[a[i] + 1] == 1:
                tval = val[find(a[i] + 1)]
                if tval[1] - tval[0] + 1 == m:
                    cnt -= 1
                union(a[i] + 1, a[i])
            tval = val[find(a[i])]
            if tval[1] - tval[0] + 1 == m:
                cnt += 1
            if cnt >= 1:
                ans = i + 1
        return ans
