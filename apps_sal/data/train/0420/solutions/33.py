class Solution:
    def flip(self, num, pos):
        if num & 2**pos:
            return num - 2**pos
        else:
            return num + 2**pos

    def findTheLongestSubstring(self, s: str) -> int:
        hash = {(0,0,0,0,0): [-1]}
        maxLen = 0
        count =  {'a': 0, 'e': 0, 'i': 0, 'u':0, 'o':0}
        
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] = (count[s[i]] + 1) % 2
            set = tuple(count.values())
            if set in hash:
                hash[set].extend([i])
            else:
                hash[set] = [i]
            if len(hash[set]) >= 2:
                maxLen = max(maxLen, hash[set][-1] - hash[set][0])
        return maxLen

