class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        hashmap = {}
        occ = {}
        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1

            if i >= minSize:
                hashmap[s[i - minSize]] -= 1
                if hashmap[s[i - minSize]] == 0:
                    del hashmap[s[i - minSize]]
            if i >= minSize - 1:
                if len(hashmap) <= maxLetters:
                    substring = s[i - minSize + 1: i + 1]
                    occ[substring] = occ.get(substring, 0) + 1

        if len(occ) == 0:
            return 0
        return max(occ.values())
