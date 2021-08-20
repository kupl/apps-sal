class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        positions = [-1]
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                positions.append(i)
        positions.append(len(nums))
        total = 0
        for i in range(1, len(positions) - k):
            num_before = positions[i] - positions[i - 1]
            num_after = positions[i + k] - positions[i + k - 1]
            total += num_before * num_after
        return total
