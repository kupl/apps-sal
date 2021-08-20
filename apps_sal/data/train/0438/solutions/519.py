class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        uf = {}
        cnt = Counter()

        def find(x):
            if uf[x][0] != x:
                uf[x][0] = find(uf[x][0])[0]
            uf[x][1] = uf[uf[x][0]][1]
            return uf[x]

        def union(x, y):
            (t1, t2) = (find(y)[1], find(x)[1])
            cnt[t1] -= 1
            cnt[t2] -= 1
            uf[find(x)[0]][1] += t1
            uf[find(y)[0]][1] += t2
            uf[find(x)[0]][0] = find(y)[0]
            cnt[find(y)[1]] += 1
        seen = [0] * (len(arr) + 1)
        n = len(arr)
        ans = -1
        for (i, a) in enumerate(arr, 1):
            seen[a] = 1
            uf.setdefault(a, [a, 1])
            cnt[1] += 1
            if a > 1 and seen[a - 1]:
                union(a, a - 1)
            if a < n and seen[a + 1]:
                union(a, a + 1)
            if cnt[m]:
                ans = i
        return ans
