class Solution:
    def subarraysWithKDistinct(self, A, K):
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, s, k):
        if not s:
            return 0
        N = len(s)
        left, right = 0, 0
        ret = 0
        counter = collections.Counter()
        counter[s[right]] += 1
        while right < N:
            if len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            else:
                right += 1
                ret += right - left
                if right < N:
                    counter[s[right]] += 1

        return ret
