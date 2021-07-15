class Solution:
    def isSubString(self, s1, s2):
        diff = 0;
        l = len(s1);
        ll = len(s2);
        if(ll - l !=1):
            return False
        i = 0;
        j = 0;
        diff =0;
        while(i < l and diff < 2):
            if(s1[i] == s2[j]):
                i += 1;
                j += 1;
            else:
                j += 1;
                diff += 1;
        if(diff > 1):
            return False
        return True;
                
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words);
        words = sorted(words, key = len)
        dp = [1]*(n);
        for i in range(n):
            j = i-1
            while(j >= 0 and (len(words[i]) - len(words[j]) <= 1)):
                if(self.isSubString(words[j], words[i])):
                    dp[i] = max(dp[i], dp[j] + 1);
                j -= 1;
        return max(dp)
                

