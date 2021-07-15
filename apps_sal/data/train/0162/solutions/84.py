class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) <= len(text2) :
            ss, ls = text1, text2
        else :
            ss, ls = text2, text1
        track = [0] * len(ss)
        
        
        for i2 in range(0, len(ls)) :
            prev = track[0]
            if ls[i2] == ss[0] :
                track[0] = 1
            for i1 in range(1, len(ss)) :
                newPrev = track[i1]
                if ls[i2] == ss[i1] :
                    track[i1] = prev + 1
                else :
                    track[i1] = max(track[i1], track[i1-1])
                prev = newPrev
        return track[-1]
                
            

