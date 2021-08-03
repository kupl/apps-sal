class Solution:
    def numSplits(self, s: str) -> int:
        dictionary = {}
        sol = 0

        for i in range(len(s)):
            dictionary[s[i]] = i
        dictionary2 = {}

        for i in range(len(s) - 1):
            dictionary2[s[i]] = i
            if i == dictionary[s[i]]:
                dictionary.pop(s[i])
            if len(dictionary) == len(dictionary2):
                sol += 1
        return sol
