class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''
        i = 0
        j = 0

        maxSize = 0
        while j < len(nums):
            k = j - 1 
            while k >= i:
                if abs(nums[k] - nums[j]) > limit:
                    i = k + 1 

                k -= 1

            maxSize = max(maxSize, (j-i+1))
            j += 1

        return maxSize

        '''

        sP = 0
        eP = 0
        minQ = collections.deque([])
        maxQ = collections.deque([])
        maxSize = 0

        while eP < len(nums):
            while minQ and minQ[-1][0] > nums[eP]:
                minQ.pop()
            minQ.append((nums[eP], eP))

            while maxQ and maxQ[-1][0] < nums[eP]:
                maxQ.pop()
            maxQ.append((nums[eP], eP))

            while abs(maxQ[0][0] - minQ[0][0]) > limit and sP < eP:
                if maxQ[0][1] <= sP:
                    maxQ.popleft()
                elif minQ[0][1] <= sP:
                    minQ.popleft()

                sP += 1
            maxSize = max(maxSize, eP - sP + 1)
            eP += 1
        return maxSize
