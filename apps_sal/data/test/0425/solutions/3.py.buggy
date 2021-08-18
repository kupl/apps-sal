import sys


def count_1(n):
    ans = 0
    while n > 0:
        if n % 2 == 1:
            ans += 1
        n //= 2
    return ans


n, p = list(map(int, input().split()))
for i in range(1, 40):
    n -= p
    if n <= 0:
        break
    if count_1(n) <= i and n >= i:
        print(i)
        return
print(-1)
