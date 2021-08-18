class Solution:
    '''
    a will quest b if
        b > 0.5 * a + 7
        b <= a
        b and a both < or > 100, or a or b is 100
    bucket sort!

    '''

    def numFriendRequests(self, ages: List[int]) -> int:
        ct = Counter(ages)

        res = 0
        for a in ct:
            for b in ct:
                if b <= 0.5 * a + 7:
                    continue
                if b > a:
                    continue
                res += ct[a] * ct[b] if a != b else ct[a]**2 - ct[a]
        return res
