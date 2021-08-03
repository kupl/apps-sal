class Solution:
    def numSplits(self, s: str) -> int:
        total_chars_1 = defaultdict(int)
        total_chars_1[s[0]] = 1

        total_chars_2 = defaultdict(int)

        splits = 0

        for i in range(1, len(s)):
            total_chars_2[s[i]] += 1

        for i in range(len(s) - 1):
            if len(total_chars_1) == len(total_chars_2):
                splits += 1

            total_chars_1[s[i + 1]] += 1
            total_chars_2[s[i + 1]] -= 1

            if total_chars_2[s[i + 1]] == 0:
                del total_chars_2[s[i + 1]]

        return splits
