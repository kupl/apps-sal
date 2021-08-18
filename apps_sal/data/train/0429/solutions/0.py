class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s_count = collections.defaultdict(int)
        g_count = collections.defaultdict(int)
        bull_cnt = 0
        for s, g in zip(secret, guess):
            if s == g:
                bull_cnt += 1
            else:
                s_count[s] += 1
                g_count[g] += 1
        cow_cnt = sum(min(s_count[x], g_count[x]) for x in g_count if x in s_count)
        return "{}A{}B".format(bull_cnt, cow_cnt)
