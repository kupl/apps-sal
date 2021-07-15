class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        index_list = []
        index_list.append(-1)
        for i in range(0, len(nums)):
            if nums[i] % 2 == 1:
                index_list.append(i)
        index_list.append(len(nums))
        if len(index_list) == 0:
            return 0
        left = 1
        right = 1
        k_count = 1
        count = 0
        while right < (len(index_list) - 1):
            if k_count == k:
                count += (index_list[left] - index_list[left - 1]) * (index_list[right + 1] - index_list[right])
                left += 1
                k_count -= 1
            else:
                k_count += 1
                right += 1
        return count
