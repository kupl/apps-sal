N, K = list(map(int, input().split()))
ans = 0
for i in range(1, N + 1):
    x = i
    p = 1
    while x < K:
        p /= 2
        x <<= 1
    ans += p
print((ans / N))
