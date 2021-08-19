class Solution:

    def knightDialer(self, n: int) -> int:
        ans = [1 for x in range(10)]
        mod = 1000000007
        for i in range(n - 1):
            (ans[0], ans[1], ans[2], ans[3], ans[4], ans[5], ans[6], ans[7], ans[8], ans[9]) = (ans[4] + ans[6], ans[8] + ans[6], ans[7] + ans[9], ans[8] + ans[4], ans[9] + ans[3] + ans[0], 0, ans[7] + ans[1] + ans[0], ans[6] + ans[2], ans[1] + ans[3], ans[4] + ans[2])
        return sum(ans) % mod
