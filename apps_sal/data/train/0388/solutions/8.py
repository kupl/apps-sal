class Solution:

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        cnt = [0] * (N + 1)
        for num in citations:
            if num > N:
                cnt[N] += 1
            else:
                cnt[num] += 1
        res = 0
        for i in range(N, 0, -1):
            res += cnt[i]
            if res >= i:
                return i
        return res
