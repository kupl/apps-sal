def possible(weights, cap, D):
    if cap <= 0:
        return False
    c = 1
    cur = 0
    for w in weights:
        if cur + w <= cap:
            cur += w
        elif w <= cap:
            c += 1
            cur = w
        else:
            return False
    print(c, cap)
    return c <= D


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        hi, lo = sum(weights), max(weights)
        mid = (hi + lo) // 2
        while lo <= hi:
            print(lo, hi, mid)
            p = possible(weights, mid, D)
            if p and not possible(weights, mid - 1, D):
                return mid
            elif not p:
                lo = mid + 1
            else:
                hi = mid
            mid = (hi + lo) // 2
        return -1
