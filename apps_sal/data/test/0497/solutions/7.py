n = int(input())
a = list(map(int, input().split()))
for i in range(n - 1):
    if a[i] != a[-1]:
        ma = n - i - 1
        break
for i in range(n - 1, 0, -1):
    if a[0] != a[i]:
        ma = max(ma, i)
print(ma)
