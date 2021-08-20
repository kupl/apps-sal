class Solution:

    def findKthBit(self, n: int, k: int) -> str:

        def helper(memo):
            ans = ''
            for c in memo:
                if c == '0':
                    ans += '1'
                else:
                    ans += '0'
            return ans
        memo = '0'
        for i in range(1, n + 1):
            memo = memo + '1' + helper(memo)[::-1]
        return memo[k - 1]
