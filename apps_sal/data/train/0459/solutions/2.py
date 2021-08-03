class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = end = maxn = 0
        alpha_dict = collections.defaultdict(int)
        for end in range(1, len(s) + 1):
            alpha_dict[s[end - 1]] += 1
            maxn = max(maxn, alpha_dict[s[end - 1]])
            if end - start > k + maxn:
                alpha_dict[s[start]] -= 1
                start += 1
        return end - start
