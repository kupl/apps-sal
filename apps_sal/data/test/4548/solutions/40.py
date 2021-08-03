n, m, x = list(map(int, input().split()))
a = list(map(int, input().split()))
k = n - 1
for i in range(m):
    if a[i] > x:
        k = i
        break
if k == 0 or k == n - 1:
    print('0')
    return
else:
    print((min(k, m - k)))
