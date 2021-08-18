class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:

        n = len(arr)
        UF = list(range(n + 2))
        SZ = [0] * (n + 2)

        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]

        def union(a, b):
            a = find(a)
            b = find(b)
            if a != b:
                if SZ[a] < SZ[b]:
                    a, b = b, a
                UF[b] = a
                SZ[a] += SZ[b]

        ans = -1
        cnt = 0

        for step, x in enumerate(arr):
            UF[x] = x
            SZ[x] = 1
            cnt -= (SZ[find(x - 1)] == m) + (SZ[find(x + 1)] == m)

            if SZ[x - 1]:
                union(x, x - 1)
            if SZ[x + 1]:
                union(x, x + 1)

            if SZ[find(x)] == m:
                cnt += 1

            if cnt > 0:
                ans = step + 1

        return ans
