(n, m) = map(int, input().split())
a = list(map(int, input().split()))
imax = 0
for i in range(1, n):
    if a[i] > a[imax]:
        imax = i
k = (a[imax] - 1) // m
i = n - 1
while i >= 0:
    if (a[i] - 1) // m == k:
        print(i + 1)
        break
    else:
        i -= 1
