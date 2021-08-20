class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        window_start = 0
        window_letters = Counter()
        substring_counts = Counter()
        for window_end in range(len(s)):
            window_letters[s[window_end]] += 1
            substring_len = window_end - window_start + 1
            while substring_len > maxSize or len(window_letters) > maxLetters:
                start_char = s[window_start]
                window_letters[start_char] -= 1
                if window_letters[start_char] == 0:
                    del window_letters[start_char]
                window_start += 1
                substring_len = window_end - window_start + 1
            while substring_len >= minSize:
                assert substring_len <= maxSize
                substring = s[window_start:window_end + 1]
                substring_counts[substring] += 1
                start_char = s[window_start]
                window_letters[start_char] -= 1
                if window_letters[start_char] == 0:
                    del window_letters[start_char]
                window_start += 1
                substring_len = window_end - window_start + 1
        print(substring_counts)
        if not substring_counts:
            return 0
        return max(substring_counts.values())
