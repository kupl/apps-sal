import heapq


class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        pv_map = {}

        def pv(val):
            v = val
            cnt = 1
            while val != 1:
                if val in pv_map:
                    pv_map[v] = cnt + pv_map[val] - 1
                    return pv_map[v]
                if val % 2 == 0:
                    val /= 2
                else:
                    val = 3 * val + 1
                cnt += 1
            pv_map[v] = cnt
            return cnt
        h = []
        for v in range(lo, hi + 1):
            p = pv(v)
            if len(h) < k:
                heapq.heappush(h, (-p, -v))
            elif p < -h[0][0]:
                heapq.heapreplace(h, (-p, -v))
        return -h[0][1]
