import math
(n, m) = [int(x) for x in input().split()]
a = []
for i in range(2, int(math.sqrt(n)) + 1):
    while n % i == 0:
        a.append(i)
        while n % i == 0:
            n //= i
if n != 1:
    a.append(n)
ans = 1
for i in a:
    k = i
    while m >= k:
        ans *= pow(i, m // k, 1000000007)
        ans %= 1000000007
        k *= i
print(ans % 1000000007)
