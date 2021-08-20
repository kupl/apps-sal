(n, k, x) = [int(z) for z in input().split()]
dela = [int(z) for z in input().split()]
ans = 0
for i in range(n - k):
    ans += dela[i]
ans += x * k
print(ans)
