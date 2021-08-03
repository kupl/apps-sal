n = int(input())
L = [int(x) for x in input().split(' ')]
L.sort()
tot = sum(L)
small = tot // n
numsmall = n - (tot - small * n)
ans = 0
for i in range(0, numsmall):
    ans += max(0, small - L[i])
for i in range(numsmall, n):
    ans += max(0, small + 1 - L[i])
print(ans)
