from bisect import bisect_right as br

n, q = list(map(int, input().split()))
stn = list(map(int, input().split()))
arro = list(map(int, input().split()))

cum = []
s = 0
for i in range(n):
    s += stn[i]
    cum.append(s)

s1 = 0
ans = 0
for i in range(q):
    if ans == 0:
        s1 = arro[i]
    else:
        s1 += arro[i]
    ind = br(cum, s1)
    ans = n - ind
    if ans == 0:
        print(n)
    else:
        print(ans)
