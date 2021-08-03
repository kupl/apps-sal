class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        charToFreq = {}
        freqToChar = {}
        for c in s:
            if c not in charToFreq:
                charToFreq[c] = 0
            charToFreq[c] += 1
        for key, value in list(charToFreq.items()):
            if value not in freqToChar:
                freqToChar[value] = []
            freqToChar[value].append(key)
        result = []
        for key in range(len(s), -1, -1):
            if key in freqToChar:
                for char in freqToChar[key]:
                    result += [char] * key
        return "".join(result)
