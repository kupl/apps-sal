import sys
input = sys.stdin.readline


n, m, d = list(map(int, input().split()))
li = list(map(int, input().split()))
x = 0
l = 0
maxx = sum(li) + (d - 1) * (m + 1)

off = maxx - n
outlist = []
for i in range(m):
    if (off) >= d:

        off -= (d - 1)
    else:
        outlist.extend([0] * (d - off - 1))
        off = 0
    outlist.extend([i + 1] * li[i])

if (off) > d:
    off -= (d - 1)
else:
    outlist.extend([0] * (d - off - 1))
    off = 0

if maxx >= n:
    print("YES")
    print(" ".join([str(a) for a in outlist]))
else:
    print("NO")
