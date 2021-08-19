(N, M, C) = map(int, input().split())
B = list(map(int, input().split()))
count = 0
for n in range(N):
    A = list(map(int, input().split()))
    total = C
    for (i, j) in zip(B, A):
        total += i * j
    if total > 0:
        count += 1
print(count)
