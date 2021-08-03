class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # want subsequence that is longest arithmetic
        # dictionary with len longest subsequence at j
        # for i in range(A):
        #    for j in range(i):
        #        diff = j - i # difference between the two
        #        dictionary[(diff, i)] = max(dictionary[(diff, i)], dictionary[(diff, j)]+1)
        #

        # (-5, 1) = 1
        # (-2, 2) = 1
        # (3, 2) = 1
        # (-7,3) = 1
        # (-2,3) = 1
        long_len_sub_at_pos = {}

        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]

                # if (diff, j) in long_len_sub_at_pos:
                #     long_len_sub_at_pos[(diff, i)] = max(long_len_sub_at_pos[(diff, i)], long_len_sub_at_pos[(diff, j)] + 1)
                # else:
                #     long_len_sub_at_pos[(diff, i)] = 2

                sub_len_at_j = long_len_sub_at_pos.get((diff, j), 1)
                long_len_sub_at_pos[(diff, i)] = max(long_len_sub_at_pos.get((diff, i), 0), sub_len_at_j + 1)

        # values in the dictionary would be the length of hte subseq
        # loop over and find the max subseq

        return max(long_len_sub_at_pos.values())
