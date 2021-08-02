n, k = [int(x) for x in input().split()]
ans = -10**15
for i in range(n):
    f, t = [int(x) for x in input().split()]
    ans = max(ans, f - max(0, t - k))
print(ans)
