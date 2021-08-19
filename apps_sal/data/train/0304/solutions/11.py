class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        counter = Counter(ages)
        ages = list(counter.keys())
        res = 0
        for a in ages:
            for b in ages:
                if b <= 0.5 * a + 7:
                    continue
                if b > a:
                    continue
                if b > 100 and a < 100:
                    continue
                if a == b:
                    res += counter[a] * (counter[a] - 1)
                else:
                    res += counter[a] * counter[b]
        return res
