(n, m) = list(map(int, input().split()))
h = list(map(int, input().split()))
cnt = [0] * n
for i in range(m):
    (a, b) = list(map(int, input().split()))
    cnt[a - 1] = max(cnt[a - 1], h[b - 1])
    cnt[b - 1] = max(cnt[b - 1], h[a - 1])
res = sum([h[i] > cnt[i] for i in range(n)])
print(res)
