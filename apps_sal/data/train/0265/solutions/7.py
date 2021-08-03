class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:

        d = {}
        d[0] = -1

        N = len(nums)

        if(N == 0):
            return 0
        L = [0 for i in range(N)]
        s = nums[0]
        d[s] = 0
        if(s == target):
            L[0] = 1
        for i in range(1, N):
            s += nums[i]
            L[i] = L[i - 1]
            if(s - target in d):
                idx = d[s - target]
                if(idx == -1):
                    L[i] = max(L[i], 1)
                else:
                    L[i] = max(L[i], L[idx] + 1)

            d[s] = i
        return L[N - 1]
