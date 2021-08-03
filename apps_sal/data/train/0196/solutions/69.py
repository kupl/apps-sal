class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        N = len(A)

        ans = cur = 0
        for x in A:
            cur = x + max(cur, 0)
            ans = max(ans, cur)

        rightsums = [None] * N
        rightsums[-1] = A[-1]
        for i in range(N - 2, -1, -1):
            rightsums[i] = rightsums[i + 1] + A[i]

        # maxright[i] = max_{j >= i} rightsums[j]
        maxright = [None] * N
        maxright[-1] = rightsums[-1]
        for i in range(N - 2, -1, -1):
            maxright[i] = max(maxright[i + 1], rightsums[i])

        leftsum = 0
        for i in range(N - 2):
            leftsum += A[i]
            ans = max(ans, leftsum + maxright[i + 1])
        if max(A) < 0:
            return max(A)
        return ans


#         total = sum(A)
#         max_sum_ending_i = [A[0]]
#         prev = max_sum_ending_i[-1]


#         for i in range(1, len(A)):
#             if prev <= 0:
#                 max_sum_ending_i.append(A[i])
#             else:
#                 max_sum_ending_i.append(max_sum_ending_i[-1]+A[i])
#             prev = max_sum_ending_i[-1]

#         min_sum_ending_i = [A[0]]
#         prev = min_sum_ending_i[-1]

#         for i in range(1, len(A)):
#             if prev >= 0:
#                 min_sum_ending_i.append(A[i])
#             else:
#                 min_sum_ending_i.append(min_sum_ending_i[-1]+A[i])
#             prev = min_sum_ending_i[-1]

#         if max(A) > 0:
#             return max(total - min(min_sum_ending_i), max(max_sum_ending_i))
#         else:
#             return max(A)
