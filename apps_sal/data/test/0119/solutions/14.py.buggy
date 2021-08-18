from operator import itemgetter


def cmpnr(a, b):
    if a[0] < b[0]:
        return True
    if a[0] > b[0]:
        return False
    return a[1] > b[1]


n = int(input())
seg = []
for i in range(n):
    a, b = list(map(int, input().split()))
    seg.append((a, b, i + 1))

seg = sorted(seg, key=lambda t: (t[0], -t[1]))

maxr = 0
maxri = 0
for a, b, i in seg:
    if b <= maxr:
        print(i, maxri)
        return

    if b > maxri:
        maxr = b
        maxri = i

print(-1, -1)
