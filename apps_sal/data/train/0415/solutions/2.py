class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        mem = {}

        def rec(index, ifSwapped):
            if index == n:
                return 0
            elif (index, ifSwapped) in mem:
                return mem[(index, ifSwapped)]
            else:
                ans = float('inf')
                # Don't swap if possible
                if A[index] > A[index - 1] and B[index] > B[index - 1]:
                    ans = min(ans, rec(index + 1, 0))
                # Swap if possible
                if A[index] > B[index - 1] and B[index] > A[index - 1]:
                    A[index], B[index] = B[index], A[index]  # Swap
                    ans = min(ans, 1 + rec(index + 1, 1))
                    A[index], B[index] = B[index], A[index]  # Swap them back
                mem[(index, ifSwapped)] = ans
                return ans

        ans = float('inf')
        ans = min(ans, rec(1, 0))
        A[0], B[0] = B[0], A[0]
        ans = min(ans, 1 + rec(1, 1))
        A[0], B[0] = B[0], A[0]

        return ans
