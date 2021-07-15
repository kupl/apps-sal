class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        def getScore(sc, tc):
            if ord(sc) <= ord(tc):
                return ord(tc) - ord(sc)
            return ord('z') - ord(sc) + 1 + ord(tc) - ord('a') 
        
        if len(s) != len(t):
            return False
        
        score_ref = dict()
        for idx in range(len(s)):
            score = getScore(s[idx], t[idx])
            if score == 0:
                continue
            score_ref[score] = score if score_ref.get(score, 0) == 0 else score_ref[score] + 26
        
        return all([score_ref[score] <= k for score in score_ref])
