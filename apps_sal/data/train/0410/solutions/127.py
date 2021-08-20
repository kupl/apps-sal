class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        def getPower(n):
            step = 0
            while n != 1:
                if n % 2 == 0:
                    n = int(n / 2)
                else:
                    n = n * 3 + 1
                step += 1
            return step
        ans = []
        for i in range(lo, hi + 1):
            ip = getPower(i)
            ans.append((ip, i))
        ans.sort()
        return ans[k - 1][1]
