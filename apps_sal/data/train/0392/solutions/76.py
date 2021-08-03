
class Solution:

    import math

    def C(self, N, r):
        return int(math.factorial(N) / (math.factorial(r) * math.factorial(N - r)))

    def numWays(self, s: str) -> int:
        counter = s.count('1')
        if counter % 3 != 0:
            return 0
        if counter == 0:
            return self.C(len(s) - 1, 2) % (10**9 + 7)

        index = []
        cnt = 0
        for ind, char in enumerate(s):
            if char == '1':
                cnt += 1
                if cnt == counter // 3:
                    index.append(ind)

                if cnt == (counter // 3) + 1:
                    index.append(ind)

                if cnt == (2 * counter // 3):
                    index.append(ind)

                if cnt == (2 * counter // 3) + 1:
                    index.append(ind)

        m = index[1] - index[0]
        n = index[3] - index[2]
        return m * n % (10**9 + 7)
