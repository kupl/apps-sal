class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        for i in range(n-2, -1,-1):
            stoneValue[i] += stoneValue[i+1]
        
        from functools import lru_cache
        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0
            return stoneValue[i] - min(dp(i+x) for x in [1,2,3])
            
        
        Alice = dp(0)
        Bob = stoneValue[0] - Alice
        
        if Alice > Bob:
            return 'Alice'
        elif Alice < Bob:
            return 'Bob'
        else:
            return 'Tie'
        
    def stoneGameIII(self, A: List[int]) -> str:
        @lru_cache(None)
        def dp(i):
            # beyond the scope, return 0
            if i>=len(A):return 0
            # if only one element left, return this value
            if i==len(A)-1:return A[-1]
            # three actions: pick up 1, pick up 2, pick up 3. 
            # alice_score_of_alice at i = 
            #  max(action_score_of_alice - (action_score_of_bob at i+j+1) for action in 3 cases)
            res = -float('inf')
            for j in range(3):
                if i+j<len(A):
                    this_res = sum(A[i:i+j+1])-dp(i+j+1)
                    res = max(res, this_res)
            return res
        
        if dp(0)>0:return 'Alice'
        elif dp(0)<0:return 'Bob'
        else:return 'Tie'
