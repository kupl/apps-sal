class Solution:
    def maxFreq(self, s: str, maxy: int, m: int, mm: int) -> int:
        
        i,j = 0,0
        count = collections.Counter()
        count[s[0]]+=1
        ans = collections.Counter()
        u, n = 1, len(s)
        
        key = s[0]
        
        while True:
            if u<=maxy and m<=i-j+1<=mm: 
                ans[key]+=1
            
            if j<i and i-j+1>=m:
                count[s[j]]-=1
                if count[s[j]]==0: u-=1
                j+=1
                key = key[1:]
            else:
                i+=1
                if i == n: break
                if count[s[i]]==0: u+=1
                count[s[i]]+=1
                key+=s[i]
            
        return max(ans.values()) if ans else 0
