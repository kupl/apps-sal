class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        def right_boundry(A, dupl):
            res = [0] * len(A)
            A.append(-math.inf)
            stack = []

            for i in range(len(A)):
                if dupl:
                    while stack and A[stack[-1]] > A[i]:
                        j = stack.pop()
                        res[j] = i - j
                else:
                    while stack and A[stack[-1]] >= A[i]:
                        j = stack.pop()
                        res[j] = i - j

                stack.append(i)

            A.pop()
            return res

        right = right_boundry(A, False)
        left = right_boundry(A[::-1], True)[::-1]

        ans = sum([right[i] * left[i] * A[i] for i in range(len(A))])

        return ans % (10**9 + 7)


#         dp = [0] * (len(A) + 1)
#         N = len(A)

#         for i in range(1,N+1):
#             mn = A[i-1]
#             dp[i] = dp[i-1]
#             for j in range(i, 0, -1):
#                 mn = min(mn, A[j-1])
#                 dp[i] = (dp[i] + mn) % (10**9 + 7)

#         return dp[-1]


#         cnt = 0
#         k = 1

#         while k <= len(A):
#             stack = []
#             for i in A:
#                 if len(stack) < k:
#                     stack.append(i)
#                     if len(stack) == k:
#                         cnt += min(stack)
#                         stack.pop(0)

#             k += 1

#         return cnt
