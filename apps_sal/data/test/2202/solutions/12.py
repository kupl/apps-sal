(n, p) = (int(x) for x in input().split())
a = [int(x) for x in input().split()]
sum1 = int(0)
sum2 = int(0)
for i in range(0, n):
    sum2 = sum2 + a[i]
k = n - 1
b = [0]
for i in range(0, k):
    sum1 = sum1 + a[i]
    sum2 = sum2 - a[i]
    b.append(sum1 % p + sum2 % p)
print(max(b))
