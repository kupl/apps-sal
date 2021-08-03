class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        c = collections.Counter(ages)

        def request(x, y):
            return not (y <= 0.5 * x + 7 or (x < 100 and y > 100) or x < y)

        ans = 0
        for x in c:
            for y in c:
                if request(x, y):
                    if x == y:
                        ans += c[x] * (c[y] - 1)
                    else:
                        ans += c[x] * c[y]
        return ans
