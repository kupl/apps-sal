c1, c2, c3, c4 = map(int, input().split())
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sum1 = 0
for i in range(n):
    sum1 += min(a[i] * c1, c2)
sum2 = 0
for i in range(m):
    sum2 += min(b[i] * c1, c2)
print(min(c4, 2 * c3, c3 + sum1, c3 + sum2, sum1 + sum2))
