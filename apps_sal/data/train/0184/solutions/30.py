class Solution:
    def maxRepOpt1(self, text: str) -> int:
        hashmap = {}
        wordlist = [] 
        l, r, ans = 0, 0, 0
        while r < len(text):
            while r < len(text) and text[l] == text[r]:
                r += 1
            wordlist.append([text[l], r-l])
            if text[l] not in hashmap:
                hashmap[text[l]] = r-l
            else:
                hashmap[text[l]] += r-l
            l = r
        for ch, count in wordlist:
            ans = max(ans, min(count+1, hashmap[ch]))
        for i in range(1, len(wordlist)-1):
            if wordlist[i-1][0] == wordlist[i+1][0] and wordlist[i][1] == 1:
                ans = max(ans, min(wordlist[i-1][1] + wordlist[i+1][1]+1, hashmap[wordlist[i+1][0]]))
        
        return ans
            

