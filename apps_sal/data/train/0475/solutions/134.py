class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sumArr, prev = [], []
        for num in nums:
            sumArr.append(num)
            temp = [num]
            for i in range(len(prev)):
                sumArr.append(num+prev[i])
                temp.append(num+prev[i])
            prev = temp
        sumArr.sort()
        return sum(sumArr[i] for i in range(left-1, right)) % (10**9 + 7)
