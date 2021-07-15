class Solution:
    def countTriplets(self, A: List[int]) -> int:
        tmp = {}
        for a in A:
            for b in A:
                if a&b in tmp:
                    tmp[a&b]+=1
                else:
                    tmp[a&b]=1        
        ans = 0
        
        for k, t in tmp.items():
            for c in A:
                if c&k==0:
                    ans +=t
        return ans
