class Solution:

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        "\n         cnt = collections.Counter(s)\n         tmp = list(k*v for k, v in cnt.items())\n         res = sorted(tmp, key=len, reverse=True)\n         return ''.join(res)\n         "
        res = ''
        cnt = collections.Counter(s)
        tmps = cnt.most_common()
        for tmp in tmps:
            res += tmp[0] * tmp[1]
        return res
