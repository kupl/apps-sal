class Solution:
    #    [9, 4, 7, 2, 10]
    #     1  2  2  2   3
    # (4, 5): 2
    # (7, 2): 2
    # (7, 3): 2
    # (2, 7): 2
    # (2, 2): 2
    # (2, 5): 2
    # (10, 1): 2
    # (10, 6): 2
    # (10, 3): 3
    # (10, 8): 2
    # store the last val in a sequence formed, its difference and length
    
    # [24, 13, 1, 100, 0, 94, 3, 0, 3] result = 2
    # (13, 11): 2
    # (1, 23): 2
    # (1, 12): 2
    # (100, 86): 2
    # (100, 87): 2
    # (100, 99): 2
    # (0, -24): 2
    # (0, -13): 2
    # (0, -1): 2
    # (0, -100): 2
    # (94, 70): 2
    # (94, 81): 2
    # (94, 93): 2
    # (94, -6): 2
    # (94, 94): 2
    # (3, -11): 2
    # (3, -10): 2
    # (3, -2): 2
    # (3, -97): 2
    # (3, 3, 7): 2
    # (3, -91): 2
    
    def longestArithSeqLength(self, A: List[int]) -> int:
        
        seqs = {} # stores mapping of (last_num_in_seq, diff) to length
        
        result = 2
        
        for i in range(1, len(A)):
            for j in range(0, i):
                diff = A[i] - A[j]
                
                if (A[j], diff, j) in seqs:
                    seqs[(A[i], diff, i)] = seqs[(A[j], diff, j)] + 1
                else:
                    seqs[(A[i], diff, i)] = 2
                    
                result = max(result, seqs[(A[i], diff, i)])
                
        return result
