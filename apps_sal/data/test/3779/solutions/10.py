def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


n, k = map(int, input().split(' '))
aa = list(map(int, input().split(' ')))

m = k
for a in aa:
    m = gcd(m, a)

print(k // m)
for i in range(0, k, m):
    print(i, end=' ')
print()
