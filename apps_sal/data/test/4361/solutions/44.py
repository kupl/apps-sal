(N, K) = list(map(int, input().split()))
h = []
ans = 1000000000
for i in range(N):
    h.append(int(input()))
h = sorted(h)
for j in range(N - K + 1):
    if ans > h[j + K - 1] - h[j]:
        ans = h[j + K - 1] - h[j]
print(ans)
