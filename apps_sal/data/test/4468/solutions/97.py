(n, k) = map(int, input().split())
t = list(map(int, input().split()))
ans = n * k
for i in range(1, n):
    diff = k - min(t[i] - t[i - 1], k)
    ans -= diff
print(ans)
