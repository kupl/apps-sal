class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        N = len(nums)
        nums.sort()
        answer = 0
        for i in range(N):
            current_num = nums[i]
            low = i + 1
            high = N - 1
            while low <= high:
                middle = (low + high) // 2
                if current_num + nums[middle] > target:
                    high = middle - 1
                else:
                    low = middle + 1
            if current_num + nums[high] <= target:
                answer += 2 ** (high - i)
        return answer % (10 ** 9 + 7)
