class Solution:

    def check(self, a, b):
        if b <= 0.5 * a + 7:
            return False
        if b > a:
            return False
        if b > 100 and a < 100:
            return False
        return True

    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = 0
        c = [0 for x in range(121)]
        for a in ages:
            c[a] += 1
        for i in range(len(c)):
            for j in range(len(c)):
                if self.check(i, j):
                    cnt += c[i] * c[j]
                    if i == j:
                        cnt -= c[i]
        return cnt
