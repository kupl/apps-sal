class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        max_freq = 0
        for l in range(minSize,maxSize+1):
            hmap = {}
            for i in range(len(s)-l+1):
                if len(set(s[i:i+l])) <= maxLetters:
                    if s[i:i+l] in list(hmap.keys()):
                        hmap[s[i:i+l]] += 1
                    else:
                        hmap[s[i:i+l]] = 1
            if list(hmap.keys()):
                max_freq = max(max_freq,max(list(hmap.items()),key=lambda kv: kv[1])[1])
        return max_freq

