class Solution:
    def maxFreq(self, s: str, maxy: int, m: int, mm: int) -> int:
        
        i,j = 0,0
        count = collections.Counter()
        count[s[0]]+=1
        ans = collections.Counter()
        u = 1
        n = len(s)
        while True:
            # print(f'j-{j}, i-{i}, u-{u}, ans-{ans}')
            if u<=maxy and m<=i-j+1<=mm: 
                # print('Found!-',j,i,s[j:i+1])
                ans[s[j:i+1]]+=1
            
            if j<i and i-j+1>=m:
                count[s[j]]-=1
                if count[s[j]]==0: u-=1
                j+=1
            else:
                i+=1
                if i == n: break
                if count[s[i]]==0: u+=1
                count[s[i]]+=1
        print(ans)
        return max(ans.values()) if ans else 0
