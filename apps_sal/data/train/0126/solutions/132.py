class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        counts = {}  # string -> number

        for current_size in range(minSize, maxSize + 1):
            window = {}
            for i in range(current_size):
                c = s[i]
                window[c] = window.get(c, 0) + 1

            for i in range(current_size, len(s) + 1):
                start = i - current_size
                if len(window) <= maxLetters:
                    sub = s[start:i]
                    counts[sub] = counts.get(sub, 0) + 1
                if i == len(s):
                    break

                # add current
                c = s[i]
                window[c] = window.get(c, 0) + 1
                # remove tail
                c = s[start]
                window[c] -= 1
                if window[c] == 0:
                    del window[c]

        # print(counts)
        return max(counts.values()) if len(counts) else 0
