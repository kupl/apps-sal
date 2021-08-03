# SELF TRY 9/20/2020
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # Problem asks -> array A
        # Want -> return the length of longest arithmetic subseq in A

        # Two cases basically.
        # When building up to to your table
        # When looking at previous values i.e from (col, change) we see that there is a PREVIOUS value already there. (With the same change) so you know you can extend that length by 1
        # This \"1\" indicates the CUR number is being added because it's change is the same.
        # If it's never been seen that the base case is at most length 2
        # i.e some \"subseq\" whatever it is with 2 elements would always be \"valid\" and so would be length 2
        table = dict()
        longest_subseq = float('-inf')

        for row in range(len(A)):
            for col in range(0, row):
                change = A[row] - A[col]
                if (col, change) in table:
                    table[(row, change)] = 1 + table[(col, change)]

                else:
                    table[(row, change)] = 2

                longest_subseq = max(longest_subseq, table[(row, change)])

        return longest_subseq


# class Solution:
#     def longestArithSeqLength(self, A):
#         d = {}
#         for i in range(1, len(A)):
#             for j in range(len(A)):
#                 delta = A[i] - A[j]
#                 d[(i, delta)] = d[(j, delta)] + 1 if (j, delta) in d else 2
#         return max(d.values())
# class Solution:
#     def longestArithSeqLength(self, A: List[int]) -> int:
#         #Array A
#         #Want return the (Len of longest arithmetic subseq in A)
#         #Recall that a subseq of A is a list A[i_1], A[i_2]... A[i_k] s.t
#         # 0 <= i_1 < i_2 < i_k <= A.len() - 1

#         #ROW
#         # [9,4,7,2,10]

#         #COL
#         #[
#         #9
#         #4
#         #7
#         #2
#         #10
#         #]
#         table = dict()
#         for row in range(1, len(A)):
#             for col in range(0, row):
#                 change = A[row] - A[col]

#                 if (col, change) in table:
#                     table[(row, change)] = table[(col, change)] + 1
#                 else:
#                     #table(1, -5) = 2
#                     #table(1, 0) = 2
#                     #table(1, -3) = 2 + 1
#                     #table(1, -2) = 2
#                     #table(1, -6) = 2
#                     #table(0, -2) = 2
#                     #(2, 0) = 2
#                     #(3,5) = 2
#                     #(2, -3) = 2

#                     table[(row, change)] = 2

#         return max(table.values())
