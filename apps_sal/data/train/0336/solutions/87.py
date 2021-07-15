class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        count_t = collections.Counter(t)
        
        for i in range(len(s)):
            
            if s[i] in count_t:
                count_t[s[i]] -= 1
                if count_t[s[i]] == 0:
                    del count_t[s[i]]
        
        #print(count_t)
        ans = 0
        
        for key,value in count_t.items():
            #print(value)
            ans += value
            
        return ans
