n = int(input())
ans = 0
for i in range(n):
    ans += (i + 1) * (n - i)
for j in range(n - 1):
    u, v = list(map(int, input().split(' ')))
    if u <= v:
        ans -= u * (n - v + 1)
    else:
        ans -= v * (n - u + 1)
print(ans)
