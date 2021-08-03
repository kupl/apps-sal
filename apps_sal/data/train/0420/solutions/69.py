class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        state, statedict = 0, {0: -1}
        voweldict = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        maxlen = 0
        for i, c in enumerate(s):
            if c in voweldict:
                state ^= voweldict[c]
            if state in statedict:
                maxlen = max(maxlen, i - statedict[state])
            else:
                statedict[state] = i
        return maxlen
