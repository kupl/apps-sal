class Solution:
    def isPredecessor(self, s1, s2):
        if len(s2) - len(s1) != 1: return False
        newcharfound = False
        for i in range(len(s2)):
            if not newcharfound:
                if i == len(s1): return True
                if s1[i] != s2[i]:
                    newcharfound = True
                    j = i
            else:
                if s1[j] != s2[i]:
                    return False
                j += 1
        return True
    
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        
        lentoword = collections.defaultdict(list)
        for i,w in enumerate(words):
            lentoword[len(w)].append((w,i))

        dp = [1 for i in range(len(words)+1)]
        dp[0] = 0 

        for i in range(1, len(words) + 1): 
            word = words[i-1]
            curlen = len(words[i-1])
            for nbor, nborindex in lentoword[curlen-1]:
                if self.isPredecessor(nbor, word):
                    dp[i] = max(dp[i], dp[nborindex+1] +1)
        return max(dp)

