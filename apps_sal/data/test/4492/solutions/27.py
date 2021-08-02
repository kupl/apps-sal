N, x = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(N - 1):
    if(a[i] > x):
        cnt += a[i] - x
        a[i] = x

    if(a[i] + a[i + 1] > x):
        cnt += a[i] + a[i + 1] - x
        a[i + 1] = x - a[i]

print(cnt)
