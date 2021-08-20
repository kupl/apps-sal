(n, m, c) = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0
for _ in range(n):
    sum = c
    a = list(map(int, input().split()))
    for i in range(m):
        sum += a[i] * b[i]
    if sum > 0:
        cnt += 1
print(cnt)
