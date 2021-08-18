import sys


def getsqs(coor, h, w):
    l = [coor[0] + x + h * (coor[1] + y - 1) for x in range(-1, 2) for y in range(-1, 2)
         if coor[0] + x > 1 and coor[0] + x < h and coor[1] + y > 1 and coor[1] + y < w]
    return l


def main(h, w, coords):
    sq = []
    ans = [0 for _ in range(10)]
    for coor in coords:
        sq.extend(getsqs(coor, h, w))
    sq.sort()
    sq.append(h * w)
    ind = 0
    for x in range(len(sq) - 1):
        if sq[x + 1] - sq[x] != 0:
            ans[x - ind + 1] += 1
            ind = x + 1
    ans[0] = max(0, (h - 2) * (w - 2) - sum(ans))
    return ans


h, w, n = list(map(int, sys.stdin.readline().strip().split()))
coords = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

for x in main(h, w, coords):
    print(x)
