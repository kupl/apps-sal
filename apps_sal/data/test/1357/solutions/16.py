n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = a[0] - 1
for i in range(1, m):
    if a[i] == a[i - 1]:
        continue
    elif a[i - 1] > a[i]:
        cnt += (n - a[i - 1]) + a[i]
    else:
        cnt += a[i] - a[i - 1]
print(cnt)
