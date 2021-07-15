n = int(input())
a = [int(x) for x in input().split()]
k = 0
while k < n and a[k] != 1:
    k += 1
m = n - 1
while m >= 0 and a[m] != 1:
    m -= 1
ans = m - k + 1
for i in range(k + 1, m):
    if a[i] == 0 and (a[i - 1] == 0 or a[i + 1] == 0):
        ans -= 1
print(max(0, ans))
