import collections
class Solution:
    def knightDialer(self, m: int) -> int:
        MOD=10**9+7
        n={0:[4,6], 1:[6,8], 2:[7,9],3:[4,8],4:[0,3,9] ,5:[] ,6:[0,1,7] ,7:[2,6],8:[1,3],9:[2,4]}
        
        end={}
        for ab in range(10):
            end[ab]=1
        for a in range(1,m):
            
            end2={}
            for ab in range(10):
                end2[ab]=0
            
            
            for key in range(10):
                val=n[key]
                # print(val)
                for c in val:
                    end2[key]+=end[c]
                # print(end2)
            end=end2
        return (sum(end.values()))%MOD

