class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        # if there's no A,
        if not A:
            return 0

        # create a dp array,
        # key would be a tuple of indices,
        dp = {}

        # iterate over the length of A,
        for it1 in range(1, len(A)):

            # iterate upto length of it1,
            for it2 in range(it1):

                # create a tuple by difference,
                key_tuple = (it2, A[it1] - A[it2])

                # if key_tuple doesn't exist,
                if key_tuple not in dp:
                    dp[(key_tuple)] = 1

                dp[(it1, A[it1] - A[it2])] = dp[(key_tuple)] + 1
        #print (dp)
        return max(dp.values())
