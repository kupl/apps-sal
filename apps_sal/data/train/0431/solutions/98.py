# class Solution:
#     def sumSubarrayMins(self, A: List[int]) -> int:
#         MOD = 10**9+7
#         N = len(A)
        
#         stack = []
#         left, right = [None]*N, [None]*N
        
#         for i in range(N):
#             while stack and A[i]<=A[stack[-1]]:
#                 stack.pop()
#             left[i] = stack[-1] if stack else -1
#             stack.append(i)
            
#         stack = []
#         for k in range(N-1,-1,-1):
#             while stack and A[k]<A[stack[-1]]:
#                 stack.pop()
#             right[k] = stack[-1] if stack else N
#             stack.append(k)
        
#         return sum((i-left[i])*(right[i]-i)*A[i] for i in range(N)) % MOD

class Solution(object):
    def sumSubarrayMins(self, A):
        MOD = 10**9 + 7

        stack = []
        ans = dot = 0
        for j, y in enumerate(A):
            # Add all answers for subarrays [i, j], i <= j
            count = 1
            while stack and stack[-1][0] >= y:
                x, c = stack.pop()
                count += c
                dot -= x * c

            stack.append((y, count))
            dot += y * count
            ans += dot
        return ans % MOD
