class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        memo = collections.defaultdict(lambda : 0)
        i = 0
        res = 0
        vowels = set('aeiou')
        for j in range(len(s)):
            if s[j] in vowels:
                memo[s[j]] += 1
            if j-i+1==k:
                res = max(res, sum(memo.values()))
                if s[i] in memo:
                    memo[s[i]] -= 1
                    if memo[s[i]] ==0:
                        del memo[s[i]]
                i += 1
        return res
            

