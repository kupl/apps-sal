from math import ceil
(n, k) = list(map(int, input().split()))
a = [0] * k
for i in range(n):
    q = int(input())
    a[q - 1] += 1
j = 0
ans = 0
for i in a:
    j += i // 2
    ans += i % 2
print(n - (ans - (ceil(n / 2) - j)))
