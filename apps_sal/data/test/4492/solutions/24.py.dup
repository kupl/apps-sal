n, x = map(int, input().split())
a = list(map(int, input().split()))
k = 0
cnt = 0

if a[1] + a[0] > x and x >= a[0]:
    k = x - a[0]
    cnt += a[1] + a[0] - x

elif a[1] + a[0] > x and x < a[0]:
    k = 0
    cnt += a[1] + a[0] - x

else:
    k = a[1]

for i in range(1, n - 1):
    if k + a[i + 1] <= x:
        k = a[i + 1]

    elif x >= k:
        cnt += k + a[i + 1] - x
        k = x - k

    else:
        cnt += k + a[i + 1] - x
        k = 0


print(cnt)
