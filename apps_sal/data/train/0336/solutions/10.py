class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hash_ = dict()

        for i in range(len(s)):
            hash_.setdefault(t[i], 0)
            hash_.setdefault(s[i], 0)
            hash_[t[i]] -= 1
            hash_[s[i]] += 1

        sum_ = 0

        for v in hash_.values():
            if v > 0:
                sum_ += v

        return sum_
