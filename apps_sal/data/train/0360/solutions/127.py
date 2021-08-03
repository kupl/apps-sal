class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        preSum = [0]
        for weight in weights:
            preSum.append(weight + preSum[-1])
        N = len(weights)

        def shipWeights(ship):
            D0 = D
            start = 0
            l = 1
            r = N
            while D0 > 0 and l <= N:
                if ship >= preSum[r] - preSum[start]:
                    l = r + 1
                while r > l:
                    m = (l + r) // 2
                    if preSum[m] - preSum[start] > ship:
                        r = m
                    else:
                        l = m + 1
                D0 -= 1
                start = l - 1
                r = N

            if l == N + 1:
                return True
            return False

        wl = max(weights)
        wr = sum(weights)

        if D >= len(weights):
            return wl
        if D == 1:
            return wr
        while wr > wl:
            wm = (wr + wl) // 2
            if shipWeights(wm):
                wr = wm
            else:
                wl = wm + 1
        return wl
