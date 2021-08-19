class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0 for _ in range(121)]
        for a in ages:
            count[a] += 1
        ans = 0
        for (a, cnt_a) in enumerate(count):
            for (b, cnt_b) in enumerate(count):
                if a <= 0.5 * b + 7:
                    continue
                if a > b:
                    continue
                if a > 100 and b < 100:
                    continue
                ans += cnt_a * cnt_b
                if a == b:
                    ans -= cnt_a
        return ans
