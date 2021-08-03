class Solution:
    def numSplits(self, s: str) -> int:

        b_c = collections.defaultdict(lambda: 0)
        a_c = dict(collections.Counter(list(s)))

        # print('initial', b_c, a_c)

        ans = 0
        for i, ch in enumerate(list(s)):
            # print(i, ch)
            b_c[ch] += 1
            a_c[ch] -= 1
            # print(b_c, a_c)

            if len({k for k, v in list(b_c.items()) if v > 0}) == len({k for k, v in list(a_c.items()) if v > 0}):
                ans += 1

        return ans
