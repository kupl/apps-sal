N, K = map(int, input().split())
x = list(map(int, input().split()))
mi = 10 ** 18
for i in range(N - K + 1):
    l = x[i]
    r = x[i + K - 1]
    lr = abs(l) + abs(l - r)
    rl = abs(r) + abs(l - r)
    mi = min(mi, min(lr, rl))
print(mi)
