N, K = map(int, input().split())
h = [0] * N
for i in range(N):
    h[i] = int(input())
h = sorted(h)
ans = 10**10
for i in range(N - (K - 1)):
    tmp = h[i + K - 1] - h[i]
    ans = min(tmp, ans)
print(ans)
