class Solution:

    def numTriplets(self, a: List[int], b: List[int]) -> int:
        n = len(a)
        m = len(b)
        pro1 = {}
        pro2 = {}
        for i in range(n):
            for j in range(n):
                if i != j:
                    pro1[a[i] * a[j]] = pro1[a[i] * a[j]] + 1 if a[i] * a[j] in pro1 else 1
        for i in range(m):
            for j in range(m):
                if i != j:
                    pro2[b[i] * b[j]] = pro2[b[i] * b[j]] + 1 if b[i] * b[j] in pro2 else 1
        ans = 0
        for i in range(n):
            if a[i] ** 2 in pro2:
                ans += pro2[a[i] ** 2] // 2
        for i in range(m):
            if b[i] ** 2 in pro1:
                ans += pro1[b[i] ** 2] // 2
        return ans
