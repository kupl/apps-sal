class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        newArray = []
        for i in range(n - 1):
            sm = nums[i]
            for j in range(i + 1, n):
                sm += nums[j]
                newArray.append(sm)
        newArray += nums
        newArray = sorted(newArray)
        
        res = 0
        for i in range(left, right + 1):
            res += newArray[i - 1]
        res = res % (10 ** 9 + 7)
        return res

