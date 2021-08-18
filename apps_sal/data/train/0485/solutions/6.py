class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:

        count = 0
        stack = []
        for i in range(len(A)):
            if stack and i == stack[0]:
                stack.pop(0)
            if A[i] == len(stack) % 2:
                if i + K > len(A):
                    return -1
                count += 1
                stack.append(i + K)

        return count
