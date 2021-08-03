from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return 0 if nums[0] == 0 else 1
        q = deque()
        num_z = 0
        maxx = 0
        is_0 = 0
        for i in range(n):
            if nums[i] == 1:
                q.append(i)
                continue
            is_0 = 1
            if num_z < 1:
                q.append(i)
                num_z += 1
                maxx = max(maxx, len(q) - 1)
                continue
            maxx = max(maxx, len(q) - 1)
            while q and num_z == 1:
                top = q.popleft()
                if nums[top] == 0:
                    num_z -= 1
            q.append(i)
            num_z += 1

        if is_0 == 0:
            return n - 1
        maxx = max(len(q) - num_z, maxx)

        return maxx
