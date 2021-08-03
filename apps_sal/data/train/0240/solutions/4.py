class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        ret = ""
        for char, freq in counter.most_common():
            ret += char * freq
        return ret
