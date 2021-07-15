from collections import Counter
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        # test = Counter(s)
        # print(\"test\", test)
        cnt = Counter()
        word_cnt = Counter()
        cur_hash = 0
#         for i in range(minSize):
#             cnt[s[i]] += 1
#             if len(cnt)>maxLetters:
#                 break
                
        # word_cnt[s[:i+1]] += 1
        # print(word_cnt)
        left = 0
        res = 0
        i = 0
        while i<len(s):
            if i-left+1>minSize:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
                
            cnt[s[i]] += 1   
            
            if len(cnt)<=maxLetters and i-left+1==minSize:
                word_cnt[s[left:i+1]] += 1
                # print(s[left:i+1])
                res = max(res, word_cnt[s[left:i+1]])
                
            i += 1
        # print(word_cnt)
        return res
# \"aababcaab\"
# 2
# 3
# 4
# \"aaaa\"
# 1
# 3
# 3
# \"aabcabcab\"
# 2
# 2
# 3
# \"abcde\"
# 2
# 3
# 3
                

