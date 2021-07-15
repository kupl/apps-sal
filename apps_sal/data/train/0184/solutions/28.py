class Solution:
    def maxRepOpt1(self, text: str) -> int:
        n = len(text)
        ans = 1
        mp = {}
        for i in text:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        for i in range(26):
            first = 0
            second = 0
            if chr(i+97) in mp:
                for j in range(0,n):
                    if text[j]==chr(97+i):
                        first+=1
                        if first+second<mp[chr(i+97)]:
                            ans = max(ans,first+second+1)
                        else:
                            ans = max(ans,first+second)
                    else:
                        if j!=0 and j!=n-1 and text[j-1]==chr(i+97) and text[j+1]==chr(i+97):
                            second = first
                        else:
                            second = 0
                        first = 0
                        
        return ans

