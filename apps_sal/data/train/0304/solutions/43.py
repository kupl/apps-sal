class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort(reverse=True)
        n = len(ages)

        def check(a, b):
            if b <= (a * 0.5) + 7:
                return False
            if b > a:
                return False
            if b > 100 and a < 100:
                return False
            return True
        res = 0
        c = collections.Counter(ages)
        for a in c:
            for b in c:
                if check(a, b):
                    res += c[a] * (c[b] - (a == b))
        return res
