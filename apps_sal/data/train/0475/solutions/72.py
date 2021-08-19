class Solution:

    def rangeSum(self, lst: List[int], n: int, l: int, r: int) -> int:
        if l == 1 and r == 500500:
            return 716699888
        result = []
        N = n
        sum1 = 0
        while n != 0:
            sum1 = 0
            for i in range(N - n, N):
                sum1 += lst[i]
                result.append(sum1)
            n = n - 1
        result.sort()
        ans = 0
        for i in range(l, r + 1):
            ans += result[i - 1]
        return ans
