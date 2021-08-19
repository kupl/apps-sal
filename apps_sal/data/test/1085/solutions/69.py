import math
n = int(input())
ans = 2


def go(n, k):
    aux = 1
    while n % k == 0:
        n /= k
    if n % k == 1:
        return True
    return False


for i in range(2, n):
    if i * i > n:
        break
    if n % i == 0:
        if go(n, i):
            ans += 1
        if i != n / i and go(n, n / i):
            ans += 1
n -= 1
for i in range(2, n):
    if i * i > n:
        break
    if n % i == 0:
        ans += 1
        if i != n / i:
            ans += 1
if n == 1:
    print('1')
else:
    print(ans)
