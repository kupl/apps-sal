n, c = list(map(int, input().split()))
a = list(map(int, input().split()))
maxi = 0
d = -1
for i in range(n - 1):
    if maxi < a[i] - a[i + 1]:
        maxi = a[i] - a[i + 1]
        d = i
if d == -1:
    print(0)
else:
    print(max(a[d] - a[d + 1] - c, 0))
