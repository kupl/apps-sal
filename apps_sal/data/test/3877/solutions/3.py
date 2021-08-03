from math import log2


n, l, r = list(map(int, input().split()))
bn = list(map(int, list(bin(n)[2:])))
ans = 0
for i in range(l, r + 1):
    ans += bn[int(log2(i & -i))]
print(ans)
