class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        ans = set()
        
        for i in range(len(text)-1): 
            for j in range(i+1, (i+len(text))//2+1): 
                if text[i:j] == text[j:2*j-i]: ans.add(text[i:j])
        
        return len(ans)
