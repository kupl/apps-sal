class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt=collections.Counter()
        for size in range(minSize, maxSize+1):
            for i in range(len(s)-size+1):
                sub=s[i:i+size]
                if len(set(sub))<=maxLetters:
                    cnt[sub]+=1
        return max(cnt.values() )   if cnt else 0          
                    

