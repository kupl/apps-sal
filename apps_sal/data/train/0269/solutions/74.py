class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        array_one = []
        for i in range(len(nums)):
            if(nums[i]):
                array_one.append(i)
        print(array_one)
        for i in range(1, len(array_one)):
            if(array_one[i] - array_one[i - 1] - 1 < k):
                return False

        return True
