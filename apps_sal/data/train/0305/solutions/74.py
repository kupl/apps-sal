class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n=len(text)
        ans=set()
        i=0
        while i<n:
            for l in range(2,n+1,2):
                mid=i+l//2
                if text[i:mid]==text[mid:i+l]:
                    ans.add(text[i:mid])
                l+=2
            i+=1
        return len(ans)
