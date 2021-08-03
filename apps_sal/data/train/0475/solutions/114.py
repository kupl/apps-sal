
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarr = []
        modu = pow(10, 9) + 7
        output = 0
        for i in range(0, len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                subarr.append(sum)
        subarr.sort()
        for i in range(left - 1, right):
            output += subarr[i]
            output = output % modu
            print((subarr[i]))
        return output
