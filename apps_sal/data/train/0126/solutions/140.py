class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        subset_d = {}

        for i in range(minSize, maxSize + 1):
            for j in range(0, len(s) - i + 1):
                substr = s[j:j + i]
                subset_d[substr] = subset_d.get(substr, 0) + 1

        max_occur = 0
        for substr, val in list(subset_d.items()):
            temp_s = set(list(substr))

            if val > max_occur and len(temp_s) <= maxLetters:
                max_occur = val

        return max_occur
