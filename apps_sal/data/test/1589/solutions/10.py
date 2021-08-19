(n, m) = list(map(int, input().split()))
cnt = 0
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(0, 2 * m, 2):
        cnt += a[j] or a[j + 1]
print(cnt)
