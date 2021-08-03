class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        counts = {}  # string -> number

        for current_size in range(minSize, maxSize + 1):
            window = {}
            for i in range(current_size - 1):
                c = s[i]
                window[c] = window.get(c, 0) + 1

            for i in range(current_size - 1, len(s)):
                start = i - current_size

                # add current
                c = s[i]
                window[c] = window.get(c, 0) + 1

                # remove tail
                if start >= 0:
                    c = s[start]
                    window[c] -= 1
                    if window[c] == 0:
                        del window[c]

                # check
                if len(window) <= maxLetters:
                    sub = s[start + 1:i + 1]
                    counts[sub] = counts.get(sub, 0) + 1

        # print(counts)
        return max(counts.values()) if len(counts) else 0
