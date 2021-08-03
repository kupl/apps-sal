N, K = list(map(int, input().split()))
p = list(map(int, input().split()))
for i in range(N):
    p[i] = (p[i] + 1) / 2
a = [0]
for i in range(N):
    a.append(a[-1] + p[i])
ans = 0
for i in range(N - K + 1):
    ans = max(ans, a[i + K] - a[i])
print(ans)
