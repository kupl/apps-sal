class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        i = 0
        j = 0
        map1 = {}
        res = {}
        while j < len(s):
            map1[s[j]] = map1.get(s[j], 0) + 1
            if len(map1.keys()) > maxLetters:
                map1[s[i]] = map1[s[i]] - 1
                if map1[s[i]] == 0:
                    del map1[s[i]]
                i += 1
            while len(map1.keys()) <= maxLetters and j - i + 1 <= maxSize and j - i + 1 >= minSize:
                # add to result first
                res[s[i:j + 1]] = res.get(s[i:j + 1], 0) + 1

                # remove the existing s[i]'s value from map

                map1[s[i]] = map1[s[i]] - 1
                if map1[s[i]] == 0:
                    del map1[s[i]]

                # move i=i+1
                i = i + 1
            j = j + 1
        if len(res) == 0:
            return 0
        else:
            maximum = max(res, key=res.get)
            return res[maximum]
