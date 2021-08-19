class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # n = len(A)
        # max_sub_ending = [A[0]]
        # max_sub_start_index = [0]

        #         A.extend(A)
        #         print(A)
        #         for i in range(1, len(A)):
        #             prev = max_sub_ending[i-1]
        #             if prev <= 0:
        #                 max_sub_start_index.append(i)
        #                 max_sub_ending.append(A[i])
        #             if i - max_sub_start_index[-1] < n:
        #                 max_sub_start_index.append(max_sub_start_index[-1])
        #                 max_sub_ending.append(A[i]+max_sub_ending[-1])
        #             elif (i - max_sub_start_index[-1]) == n:
        #                 index_len = len(max_sub_start_index)
        #                 val = max_sub_start_index[index_len-n]
        #                 current_sum = max_sub_ending[-1] - val
        #                 if current_sum <= 0:
        #                     max_sub_start_index.append(i)
        #                     max_sub_ending.append(A[i])
        #                 else:
        #                     max_sub_start_index.append(max_sub_start_index[-1]+1)
        #                     max_sub_ending.append(A[i]+current_sum)
        #         print(max_sub_ending)
        #         return max(max_sub_ending)
        n = len(A)
        max_sub_ending = [A[0]]
        max_sub_ending_index = [0]

        for i in range(1, len(A)):
            prev = max_sub_ending[i - 1]
            if prev <= 0:
                max_sub_ending_index.append(i)
                max_sub_ending.append(A[i])
            else:
                max_sub_ending_index.append(max_sub_ending_index[-1])
                max_sub_ending.append(A[i] + max_sub_ending[-1])
        print(max_sub_ending)
        posmax = max(max_sub_ending)
        total = sum(A)

        for i in range(len(A)):
            A[i] = -A[i]
        max_sub_ending = [A[0]]
        max_sub_ending_index = [0]

        for i in range(1, len(A)):
            prev = max_sub_ending[i - 1]
            if prev <= 0:
                max_sub_ending_index.append(i)
                max_sub_ending.append(A[i])
            else:
                max_sub_ending_index.append(max_sub_ending_index[-1])
                max_sub_ending.append(A[i] + max_sub_ending[-1])
        print(max_sub_ending)
        negmax = max(max_sub_ending) + total
        if negmax > posmax and negmax != 0:
            return negmax
        else:
            return posmax

#         cycle = max_sub_ending[-1]
#         if cycle <= 0:
#             return max(max_sub_ending)

#         for i in range(max_sub_ending_index[-1]):
#             if cycle <= 0:
#                 return max(max_sub_ending)

#             max_sub_ending_index[i] = cycle+A[i]
#             cycle = max_sub_ending_index[i]
#         return max(max_sub_ending)

#         total = sum(A)

#         #left sum
#         left_sum = [A[0]]
#         left = A[0]

#         for i in range(1, len(A)):

#             left = left+A[i]
#             left_sum.append(left)

#         #right sum
#         right = A[-1]
#         right_sum = [right]

#         for i in range(len(A)-2, -1, -1):

#             right += A[i]
#             right_sum.append(right)

#         right_sum.reverse()

#         max_sub = total

#         for i in range(0, len(A)):
#             for j in range(i, len(A)):
#                 left, right = 0, 0
#                 if i != 0:
#                     left = left_sum[i-1]
#                 if j != (len(A) -1):
#                     right = right_sum[j+1]
#                 max_sub = max(max_sub, total - left - right , left+right)

#         #corner case
#         if max(A) < 0:
#             return max(A)
#         return max_sub
