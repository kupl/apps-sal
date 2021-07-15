class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        # O(N^3) to try oring every possible subarray
        
        # key fact: for any number k , k | k = k
        # also 0 | k = k for all k
        
        # one small optimization: scan through and delete any 0s or consecutive repeats
        
        # keep a list of or results s.t. or[i] = set of all possible results from oring subarrays that end at i
        # then or[i] = [A[i]] + [A[i] | res for res in or[i - 1]] -> use a set to prune dups at each step
        #    you can just keep or[i] for most recent two i's
        # 
        if not A:
            return []
        # [1, 2, 4]
        # all_outcomes: {1, 2, 3, 4, 6, 7}
        # outcomes: {2, 3}
        # 4: temp {4, 6, 7}
        
        # todo(mywang): preprocess array and remove unnecessary stuff
        for i in range(len(A))[::-1]:
            if (i > 0 and A[i] == A[i - 1]):
                A.pop(i)
        all_outcomes = set()
        outcomes = set()
        for elt in A:
            outcomes = {elt} | {elt | val for val in outcomes}
            all_outcomes |= outcomes
        
        return len(all_outcomes)
