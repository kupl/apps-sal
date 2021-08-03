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

            # This loop is used because if there is [2,-1,2] and K=3 for cums=[0,2,1,3] we know that from 2 to 1 the value decreased from 1 to x increased so the min will be from 1 to x rather than 2 to x so eliminated(because length b/w 1 to x < 2 to x)

        if min1 == float('inf'):
            return -1
        return min1
