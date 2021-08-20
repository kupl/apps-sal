(N, M) = list(map(int, input().split()))
min_i = 0
max_i = N + 1
for _ in range(M):
    (a, b) = list(map(int, input().split()))
    min_i = max(min_i, a)
    max_i = min(max_i, b + 1)
c = max(max_i - min_i, 0)
print(c)
