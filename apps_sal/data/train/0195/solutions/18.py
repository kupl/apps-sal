class Solution:

    def countTriplets(self, A: List[int]) -> int:
        cnt = collections.defaultdict(int)
        for i in A:
            for j in A:
                cnt[i & j] += 1
        res = 0
        for i in A:
            for j in cnt:
                if i & j == 0:
                    res += cnt[j]
        return res
