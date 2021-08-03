n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

cnt = a[0]

if n % 2 == 0:
    for i in range(1, n // 2):
        cnt += a[i] * 2
else:
    for i in range(1, (n - 1) // 2):
        cnt += a[i] * 2
    cnt += a[(n - 1) // 2]

print(cnt)
