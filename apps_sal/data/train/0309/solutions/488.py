class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        from collections import defaultdict
        opt = defaultdict(lambda : defaultdict(int))
        l = len(A)
        
        sol = 0
        # print(opt[-4])
        
        for i in range(l): # 6
            # print(opt[-17])
            for j in range(i + 1, l): # 8
                diff = A[j] - A[i] # 0
                
                sub_l = 2                
                if diff in opt[i]:
                    sub_l = opt[i][diff] + 1
                
                opt[j][diff] = max(opt[j][diff], sub_l)
                sol = max(sol, opt[j][diff])
                # if opt[A[i]][diff] == 7:
                #     print(i, A[i], diff)
        # for i, row in enumerate(opt):
        #      print(i, row)
        
        # print(dict(opt))
        # print(opt[-4])
        # for k, v in opt.items():
        #     print(k, v) 
            # if k < 0:                
            #     print(k, v) 
        #     pass
        return sol
                        

