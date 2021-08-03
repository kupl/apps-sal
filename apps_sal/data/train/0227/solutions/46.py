class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # find the maximum subarray with max of K 0's
        # this will help find the maximum number of 1s

        # [1,1,1,0,0,0,1,1,1,1,0]
        # fast = 5
        # slow  = 0
        # lastZero = 3, 4, 5
        # slow = 3
        slow = fast = 0
        maxOnes = -1
        lastZero = collections.deque()
        while fast < len(A):
            if A[fast] == 0:
                lastZero.append(fast)
                if len(lastZero) > K:
                    slow = lastZero.popleft() + 1
            fast += 1
            maxOnes = max(maxOnes, (fast - slow))

        if maxOnes == -1:
            return len(A)
        return maxOnes
