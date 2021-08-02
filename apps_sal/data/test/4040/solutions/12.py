import sys
# input = sys.stdin.buffer.readline
input = sys.stdin.readline


n, m, d = list(map(int, input().split()))
li = list(map(int, input().split()))
x = 0
l = 0
maxx = sum(li) + (d - 1) * (m + 1)

off = maxx - n
# print(maxx,off)
outlist = []
for i in range(m):
    # print(off,d)
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
# print(l)
