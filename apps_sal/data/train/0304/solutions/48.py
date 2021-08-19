class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:

        def cond(a, b):
            return not (b <= 0.5 * a + 7 or b > a or (b > 100 and a < 100))
        freq = Counter(ages).items()
        cnt = 0
        for (a, r) in freq:
            for (b, c) in freq:
                if cond(a, b):
                    if a == b:
                        cnt += r * (r - 1)
                    else:
                        cnt += r * c
        return cnt
