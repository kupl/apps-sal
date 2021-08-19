from math import ceil
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= i
for i in range(n):
    a[i] = ceil(a[i] / n)
ans = -1
s = 10 ** 9 + 7
for i in range(n):
    if a[i] < s:
        s = a[i]
        ans = i + 1
print(ans)
