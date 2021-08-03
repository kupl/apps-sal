N = int(input())
XS = [int(i) for i in input().split()]

sxs = sorted(XS)
a1 = sxs[N // 2 - 1]
a2 = sxs[N // 2]

for i in range(N):
    x = XS[i]
    if x <= a1:
        print(a2)
    else:
        print(a1)
