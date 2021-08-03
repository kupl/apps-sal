n, k = map(int, input().split())
f = sorted(list(map(int, input().split())), reverse=True)
ans = 0
for i in range(0, n, k):
    ans += 2 * (f[i] - 1)
print(ans)
