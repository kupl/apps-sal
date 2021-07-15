N, L = map(int, input().split())
ans = 0
mn = 300000
for i in range(1, N + 1):
    x = L + i - 1
    ans += x
    if abs(x) < abs(mn):
        mn = x
print(ans - mn)
