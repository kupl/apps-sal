class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # 9 ,4    ,     7,         10
        #    ^
#             (1,-5): 2  (2, 3): 2   (3, 3):3
#                                    (3, -5):3
        
        dict = collections.defaultdict(lambda: 0)
        
        for i in range(len(A) - 1):    
            for j in range(i + 1, len(A)):
                dict[(j, A[j] - A[i])] = dict.get((i, A[j] - A[i]), 1) + 1
        
        return max(dict.values())
        

