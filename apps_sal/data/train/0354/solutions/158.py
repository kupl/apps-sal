class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        def helper(currentIndex, n, rollMax, pre,d):
            if currentIndex==n:
                return 1
            elif currentIndex>n:
                return 0
            count = 0
            if (currentIndex,pre) in d: #if this state is already calculated, return the ans
                return d[(currentIndex,pre)]
            for index in range(6):
                if index!=pre:
                    for repeat in range(1,rollMax[index]+1):
                        count+=helper(currentIndex+repeat,n,rollMax,index,d)
            d[(currentIndex,pre)]=count   #save the computation
            return count
        
        rolledCount = [0]*6  #no rolls made yet
        MOD = 10**9+7
        d = {}  #dictionary to save the states
        return helper(0,n,rollMax,-1,d)%MOD
    

        
        
#         memo = {}
#         def dfs(last, s,  k):
#             if k == n:
#                 return 1
#             if (last, s, k) not in memo:
#                 res = 0
#                 for i in range(6):
#                     if i == last:
#                         if s + 1 > rollMax[i]:
#                             continue
#                         else:
#                             res += dfs(i, s+1, k+1)
#                     else:
#                         res += dfs(i, 1, k+1)
#                 memo[last, s, k] = res
#             return memo[last, s, k]
        
        
#         return dfs(None, 0, 0)%(10**9 + 7)

