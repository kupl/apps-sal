t = [[-1 for i in range(10001)] for j in range(101)]

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        if N == 0 or N == 1:
            return N

        if K == 1:
            return N

        if t[K][N] != -1:
            return t[K][N]

        mn, l, h = sys.maxsize, 1, N
        while l <= h:
            mid = (l + h) // 2

            down_temp = self.superEggDrop(K - 1, mid - 1)
            up_temp = self.superEggDrop(K, N - mid)

            res = 1 + max(down_temp, up_temp)

            if down_temp < up_temp:
                l = mid + 1
            else:
                h = mid - 1

            mn = min(mn, res)

        t[K][N] = mn

        return mn
