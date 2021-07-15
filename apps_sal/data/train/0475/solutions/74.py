class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        temp = []
        for i in range(n):
            summ = 0
            for j in nums[i:]:
                summ += j
                temp.append(summ)
        temp.sort()
        result = int(sum(temp[left-1:right])%(10**9+7))
        return result
        

