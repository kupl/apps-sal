class Solution:
    def knightDialer(self, n: int) -> int:
        dct={0:[4,6],1:[6,8],2:[7,9],3:[4,8],4:[0,3,9],5:[],6:[0,1,7],7:[2,6],8:[1,3],9:[2,4]}
        
        def func(k):
            
            if k==1:
                return {i:1 for i in range(10)}
                        
            res=func(k-1)
            
            counts={i:0 for i in range(10)}
            
            for i in range(10):
                for t in dct[i]:
                    counts[t]+=res[i]
                    
            return counts
        
        
        res=func(n)
        
        return sum(res.values())%(10**9+7)
