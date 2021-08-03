n, k, M, D = list(map(int, input().split()))
max_ = 0
for i in range(1, D + 1):
    max_ = max(max_, i * (min(M, n // (i * k - k + 1))))
print(max_)
