'''
uniq<=max
len(sub)>=min and <=max
'''


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        hash, w_hash, res = {}, {}, float('-inf')
        self.initial_fill(s, minSize, hash)
        for i in range(0, len(s) - minSize + 1):
            if len(hash) <= maxLetters:
                string = s[i:i + minSize]
                w_hash[string] = 1 if string not in w_hash else w_hash[string] + 1
                res = max(res, w_hash[string])
            char = s[i]
            if hash[char] == 1:
                del hash[char]
            else:
                hash[char] -= 1
            if i + minSize < len(s):
                char = s[i + minSize]
                hash[char] = 1 if char not in hash else hash[char] + 1
        return res if res != float('-inf') else 0

    def initial_fill(self, s, Min, hash):
        for i in range(0, Min):
            char = s[i]
            hash[char] = 1 if char not in hash else hash[char] + 1
