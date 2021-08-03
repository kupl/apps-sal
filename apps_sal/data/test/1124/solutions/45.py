def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


n = int(input())
a = list(set([int(i) for i in input().split()]))
res = a[0]
for i in range(1, len(a)):
    res = gcd(res, a[i])
print(res)
