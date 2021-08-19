class Solution:

    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        p = [0]
        for i in A:
            p.append(p[-1] + i)
        cnt = collections.Counter()
        res = 0
        for i in p:
            res += cnt[i]
            cnt[i + S] += 1
        return res
