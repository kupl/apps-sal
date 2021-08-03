class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        for i in range(minSize, maxSize + 1):
            max_freq = self.maxFreqSetSize(s, maxLetters, i)
            if max_freq > 0:
                return max_freq
        return 0

    def maxFreqSetSize(self, s, maxLetters, windowSize):
        valid_substrings = set()
        maxFreq = 0
        for i in range(len(s) - windowSize):
            substring = s[i:i + windowSize]
            if substring in valid_substrings:
                continue
            unique_letters = set()
            for k in range(windowSize):
                letter = s[i + k]
                unique_letters.add(letter)
            if len(unique_letters) > maxLetters:
                continue
            frequency = 1
            pos = i + 1
            while pos > -1:
                new_pos = s[pos:].find(substring)
                if new_pos == -1:
                    break
                frequency += 1
                pos += new_pos + 1

            if frequency > maxFreq:
                maxFreq = frequency
            valid_substrings.add(substring)
        return maxFreq
