class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        di = defaultdict(list)
        for w in words:
            di[len(w)].append(w)
        L, U = min(di.keys()), max(di.keys())
        dp = [1] * len(di[L])
        ans = 1
        
        def ispred(w1, w2):
            skip = False
            for i in range(len(w1)):
                while w1[i] != w2[i + skip]:
                    if skip:
                        return False
                    skip = True
            return True
        
        for l in range(L+1, U+1):
            old = dp
            dp = [1] * len(di[l])
            for j, w2 in enumerate(di[l]):
                tmp = [old[i] for i, w1 in enumerate(di[l-1]) if ispred(w1, w2)]
                if tmp: dp[j] = max(tmp) + 1
            ans = max(ans, max(dp))
            
        return ans

