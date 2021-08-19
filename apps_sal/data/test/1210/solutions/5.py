(n, p) = map(int, input().split())
prob = [0.0] * n
for i in range(n):
    (l, r) = map(int, input().split())
    prob[i] = 1.0 - (r // p - (l - 1) // p) / (r - l + 1)
ans = 0.0
for i in range(n - 1):
    ans += (1.0 - prob[i] * prob[i + 1]) * 2000
ans += (1.0 - prob[n - 1] * prob[0]) * 2000
print(ans)
