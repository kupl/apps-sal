class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        c = collections.Counter(ages)
        count = 0

        for a in c:
            for b in c:
                result = self.request(a, b)
                if result:
                    continue

                count += c[a] * c[b]
                if a == b:
                    count -= c[b]
        return count

    def request(self, a, b):
        return (b <= 0.5 * a + 7 or b > a or a < 100 < b)
