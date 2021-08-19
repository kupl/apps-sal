class Solution:

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        mapping = {}
        for c in s:
            mapping[c] = mapping[c] + 1 if c in mapping else 1
        bucket = [[] for _ in range(len(s) + 1)]
        for (c, freq) in mapping.items():
            bucket[freq].append(c)
        res = ''
        for i in range(len(s), -1, -1):
            for c in bucket[i]:
                for _ in range(i):
                    res += c
        return res
