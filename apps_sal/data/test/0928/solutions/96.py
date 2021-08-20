(N, K) = list(map(int, input().split()))
a = list(map(int, input().split()))
total = 0
cnt = 0
i = 0
j = 0
while i < N:
    while total < K and j < N:
        total += a[j]
        j = j + 1
    if total >= K:
        cnt += N - j + 1
    total -= a[i]
    i = i + 1
print(cnt)
