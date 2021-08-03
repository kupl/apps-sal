class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sumarr = [nums[0]] * n
        for i in range(1, n):
            sumarr[i] = sumarr[i - 1] + nums[i]

        ansarr = []

        for i in range(n):
            for j in range(i, n):
                x = sumarr[j] - (sumarr[i - 1] if i > 0 else 0)
                ansarr.append(x)

        ansarr.sort()
        ans = 0
        for i in range(left - 1, right):
            ans += ansarr[i]

        modfac = 10**9 + 7
        return ans % modfac
