from math import gcd
(n, m) = list(map(int, input().split()))
x = list(map(int, input().split()))
p = list(map(int, input().split()))
first = x[0]
x = [x[i + 1] - x[i] for i in range(n - 1)]
a = x[0]
for i in x[1:]:
    a = gcd(a, i)
for (index, i) in enumerate(p):
    if a % i == 0:
        print('YES')
        print(first, index + 1)
        break
else:
    print('NO')
