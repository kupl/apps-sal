n = int(input())
a = list(map(int, input().split()))
m1 = sum(a) // n
m2 = (sum(a) + n - 1) // n

res1 = 0
res2 = 0
for i in range(n):
    res1 += (a[i] - m1) ** 2
    res2 += (a[i] - m2) ** 2

print((min(res1, res2)))
