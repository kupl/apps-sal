class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque()
        q.append((nums[0],0))
        max_sum = nums[0]

        for i in range(1,len(nums)):
            while q and q[0][1] < i - k:
                q.popleft()

            next_val = max(nums[i], nums[i] + q[0][0])
            
            while q and q[-1][0] < next_val:
                q.pop()

            q.append((next_val,i))

            max_sum = max(max_sum, q[0][0])

        return max_sum


