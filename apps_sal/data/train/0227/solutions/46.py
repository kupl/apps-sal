class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:

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
