class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = {}
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

        res = ""
        while counter:
            m = max(counter, key=counter.get)
            res += m * counter[m]
            del counter[m]
        return res
