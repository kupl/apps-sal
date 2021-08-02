# 803D
def do():
    k = int(input())
    ad = input()

    def valid(width, limit):
        l = -1
        count = 0
        cur = 0
        for r in range(len(ad)):
            if ad[r] == " " or ad[r] == "-":
                l = r
            cur += 1
            if cur == width:
                if l == -1 and r != len(ad) - 1:
                    return False
                count += 1
                if r == len(ad) - 1:
                    cur = 0
                else:
                    cur = r - l
                l = -1
                if count > limit:
                    return False
        if cur:
            count += 1
        return count <= limit

    lo, hi = 1, len(ad) + 1
    while lo < hi:
        mi = (lo + hi) >> 1
        if not valid(mi, k):
            lo = mi + 1
        else:
            hi = mi
    return lo


print(do())
