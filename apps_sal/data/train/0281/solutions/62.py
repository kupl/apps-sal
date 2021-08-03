class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        cnt = collections.defaultdict(int)
        for i in range(len(s)):
            if s[i] == t[i]:
                continue

            shift = 0
            if ord(t[i]) < ord(s[i]):
                shift = ord(t[i]) - ord(s[i]) + 26
            else:
                shift = ord(t[i]) - ord(s[i])

            cnt[shift] += 1

        for r in cnt:
            # We have cnt[r] letters in s that will need to be shifted r letters to line up with t.
            # We then simply need to check that k is large enough so that there are enough instances
            # of i, 1 <= i <= k, such that i % 26 == r.
            # How do we check? Well if x * 26 + r <= k, then we have (0*26 + r) % 26 == r,
            # (1*26 + r) % 26 == r, (2*26 + r) % 26 == r, ..., (x*26 + r) % 26 == r, i.e there are x + 1
            # instances of i such that i % 26 == r.
            # Given cnt[r] letters that need to be shifted, we only need to make sure that:
            #   (cnt[r]-1)*26 +r <= k
            #
            if (cnt[r] - 1) * 26 + r > k:
                return False
        return True
