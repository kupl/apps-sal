class Solution:
    def shortestSubarray(self, nums: List[int], K: int) -> int:
        sum1 = 0
        flag = False
        min1 = float('inf')
        cums = [0]
        dq = collections.deque()

        for i in range(len(nums)):
            cums.append(cums[-1] + nums[i])
        print(cums)

        for i in range(len(nums) + 1):
            while dq and cums[i] - cums[dq[0]] >= K:
                val = dq.popleft()
                min1 = min(min1, i - val)
            while dq and cums[i] <= cums[dq[-1]]:
                dq.pop()
            dq.append(i)

        if min1 == float('inf'):
            return -1
        return min1
