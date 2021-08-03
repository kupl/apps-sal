n = int(input())
a = list(map(int, input().split()))
k = a[1] - a[0]
tr = True
for i in range(2, n):
    if k != a[i] - a[i - 1]:
        tr = False
if tr:
    print(a[-1] + k)
else:
    print(a[-1])
