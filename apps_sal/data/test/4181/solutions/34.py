n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0
for i in range(n):
    c = b[i] - a[i]
    if c <= 0:
        cnt += b[i]
    else:
        d = b[i] - a[i + 1] - a[i]
        if d <= 0:
            cnt += b[i]
            a[i + 1] -= c
        else:
            cnt += a[i] + a[i + 1]
            a[i + 1] = 0
print(cnt)
