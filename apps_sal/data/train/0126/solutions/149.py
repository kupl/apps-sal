class Solution:

    def maxFreq(self, s, maxLetters, minSize, maxSize):
        result = 0
        subStringFreq = collections.defaultdict(int)
        window = collections.defaultdict(int)
        low = 0
        high = 0
        while high < len(s):
            window[s[high]] += 1
            if high - low + 1 == minSize:
                if len(window) <= maxLetters:
                    subStringFreq[s[low:high + 1]] += 1
                    result = max(result, subStringFreq[s[low:high + 1]])
                window[s[low]] -= 1
                if window[s[low]] == 0:
                    del window[s[low]]
                low += 1
            high += 1
        return result
