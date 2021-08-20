class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        (r, R) = (0, sorted(([x - r, x + r] for (x, r) in enumerate(ranges))) + [[9 ** 9]])
        did = can = count = 0
        for x in range(n):
            while R[r][0] <= x:
                can = max(can, R[r][1])
                r += 1
            if did == x:
                if can <= x:
                    return -1
                did = can
                count += 1
                if did == n:
                    break
        return count
