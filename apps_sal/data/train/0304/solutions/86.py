class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = collections.Counter(ages)
        
        res = 0
        for p1 in cnt:
            for p2 in cnt:
                # print(cnt, p1, p2, res)
                if p2 <= 0.5 * p1 + 7 or p2 > p1 or (p2 > 100 and p1 < 100):
                    continue
                if p1 == p2:
                    res += (cnt[p1]-1)*cnt[p1]
                else:
                    res += cnt[p1] * cnt[p2]

        return res

