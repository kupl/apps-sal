import heapq


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxd = collections.deque()
        mind = collections.deque()
        i = 0
        N = len(nums)
        Lm = 0
        for j in range(N):
            a = nums[j]
            while maxd and maxd[-1] < a:
                maxd.pop()
            maxd.append(a)

            while mind and mind[-1] > a:
                mind.pop()
            mind.append(a)

            while maxd[0] - mind[0] > limit:
                if maxd[0] == nums[i]:
                    maxd.popleft()
                if mind[0] == nums[i]:
                    mind.popleft()
                i += 1
            Lm = max(Lm, j - i + 1)

        return Lm
