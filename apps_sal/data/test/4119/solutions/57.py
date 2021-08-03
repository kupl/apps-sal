n, m = [int(i) for i in input().split()]

x = [int(i) for i in input().split()]

x.sort()

sa = []

for i in range(1, m):
    sa.append(x[i] - x[i - 1])

sa.sort()

ans = 0

for i in range(max(0, m - n)):
    ans += sa[i]
print(ans)
