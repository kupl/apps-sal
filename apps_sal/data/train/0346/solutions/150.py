class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [num % 2 for num in nums]
        count = 0
        indexlist = deque()
        for i in range(len(nums)):
            if nums[i] == 1:
                indexlist.append(i)
        for i in range(len(indexlist)):
            if i != 0:
                left = indexlist[i - 1] + 1
            else:
                left = 0
            if i + k - 1 > len(indexlist) - 1:
                break
            if i + k - 1 != len(indexlist) - 1:
                right = indexlist[i + k - 1 + 1] - 1
            else:
                right = len(nums) - 1
            leftdis = indexlist[i] - left + 1
            rightdis = right - indexlist[i + k - 1] + 1
            print((leftdis, rightdis, left, right))
            count += leftdis * rightdis
        return count
