class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u']
        max_cnt=sum([1 for i in range(k) if s[i] in vowels])
        cnt=max_cnt
        for i in range(k,len(s)):
            if s[i] in vowels:
                cnt+=1
            if s[i-k] in vowels:
                cnt-=1
            max_cnt=max(cnt,max_cnt)
        return max_cnt

