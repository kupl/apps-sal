class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substrings = defaultdict(int)
        char_counts = Counter(s[0:minSize - 1])
        start = 0
        while start <= len(s) - minSize:
            end = start + minSize - 1
            end_char = s[end]
            char_counts[end_char] += 1
            unique_chars = len(char_counts)
            if unique_chars <= maxLetters:
                substrings[s[start:end + 1]] += 1
            start_char = s[start]
            if char_counts[start_char] == 1:
                del char_counts[start_char]
            else:
                char_counts[start_char] -= 1
            start += 1
        maxSubstrings = 0
        for substring in substrings:
            if substrings[substring] > maxSubstrings:
                maxSubstrings = substrings[substring]
        return maxSubstrings
