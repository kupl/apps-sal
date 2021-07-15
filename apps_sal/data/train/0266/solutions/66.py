class Solution:
    def make_hist(self, array : str) -> dict:
        hist = {}
        for s in array:
            if s not in list(hist.keys()):
                hist[s] = 1
            else:
                hist[s] += 1
        return hist
    
    def numSplits(self, s: str) -> int:
        hist_left = self.make_hist(s[:1])
        hist_right = self.make_hist(s[1:])
        count = 0
        for i in range(1, len(s)):
            v = s[i]
            if len(list(hist_left.keys())) == len(list(hist_right.keys())):
                count += 1
            if v not in list(hist_left.keys()):
                hist_left[v] = 1
            else:
                hist_left[v] += 1
                
            if v in list(hist_right.keys()):
                if hist_right[v] == 1:
                    del hist_right[v]
                else:
                    hist_right[v] -= 1
        return count
            

