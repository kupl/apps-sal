class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        
        def solve(t1,t2):
            if t1 == len(text1) or t2 == len(text2):
                return 0
            
            #check cache
            if (t1,t2) in cache:
                return cache[(t1,t2)]
            
            #case1
            if text1[t1] == text2[t2]:
                opt1 = solve(t1+1,t2+1)
                cache[(t1+1,t2+1)] = opt1
                return 1 + opt1
            
            #case2
            else:
                opt1 = solve(t1,t2+1)
                opt2 = solve(t1+1,t2)
                cache[(t1,t2+1)] = opt1
                cache[(t1+1,t2)] = opt2
                return max(opt1,opt2)
                
        return solve(0,0)
