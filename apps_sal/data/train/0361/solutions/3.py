class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        d = gcd(n, m)
        if d != 1:
            return self.tilingRectangle(n // d, m // d)
        if n > m:
            n, m = m, n
        if m % n == 0:
            return m // n
        heights = [0] * n
        recs = [[0, 1]]

        CAP = max(n, m)
        ans = CAP

        def is_valid():
            if len(recs) > ans - 1:
                return False
            i, side = recs[-1]
            if heights[i] + 1 > m:
                return False
            if i + side > n:
                return False
            if heights[i + side - 1] > heights[i]:
                return False
            return True

        while recs:
            if is_valid():
                i, side = recs[-1]
                for k in range(i, i + side - 1):
                    heights[k] += 1
                heights[i + side - 1] += side
                _, i = min((heights[k], k) for k in range(n))

                if heights == [m] * n:
                    ans = min(ans, len(recs))

                recs.append([i, 1])

            else:
                i, side = recs.pop()
                for k in range(i, i + side - 1):
                    heights[k] -= side - 1

                if recs:
                    recs[-1][-1] += 1

        return ans


def gcd(a, b):
    while a:
        a, b = b % a, a
    return b
