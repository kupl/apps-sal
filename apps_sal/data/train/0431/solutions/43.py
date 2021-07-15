class Solution:
    # def sumSubarrayMins(self, A: List[int]) -> int:
    #     mins = []
    #     for i, x in enumerate(A):
    #         mins.append(x)
    #         current_min = x
    #         for j in range(i+1, len(A)):
    #             if A[j] < current_min:
    #                 current_min = A[j]
    #             mins.append(current_min)
    #     # print(mins)
    #     return int((sum(mins) % (10**9 + 7)))
    def sumSubarrayMins(self, A: List[int]) -> int:
        ple_stack = []
        left = [-1] * len(A)
        for i in range(len(A)):
            # print(ple_stack)
            while ple_stack and A[i] < A[ple_stack[-1]]:
                ple_stack.pop()
            left[i] = ple_stack[-1] if ple_stack else -1
            # print(left)
            ple_stack.append(i)
        for i in range(len(A)):
            left[i] =  i - left[i]
        # print(left)
        
        
        nle_stack = []
        right = [-1] * len(A)
        for j in reversed(range(len(A))):
            # print(nle_stack)
            while nle_stack and A[j] <= A[nle_stack[-1]]:
                nle_stack.pop()
            right[j] = nle_stack[-1] if nle_stack else len(A)
            # print(right)
            nle_stack.append(j)
        for j in range(len(A)):
            right[j] = right[j] - j
        # print(right)
        
        return sum([x * y * z for x, y, z in zip(left, right, A)]) % (10**9 + 7)
