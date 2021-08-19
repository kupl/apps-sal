import sys


def solve():
    (k, n) = list(map(int, sys.stdin.readline().split()))
    mks = list(map(int, sys.stdin.readline().split()))
    pts = list(map(int, sys.stdin.readline().split()))
    for i in range(1, k):
        mks[i] = mks[i - 1] + mks[i]
    mks = sorted(mks)
    pts = sorted(pts)
    vals = set()
    for i in range(k - n + 1):
        cand = pts[0] - mks[i]
        j = 0
        off = 0
        while j < len(pts):
            while i + j + off < k and pts[j] - cand > mks[i + j + off]:
                off += 1
            if i + j + off < k and pts[j] - mks[i + j + off] == cand:
                j += 1
            else:
                break
        if j == len(pts):
            vals.add(cand)
    print(len(vals))


solve()
