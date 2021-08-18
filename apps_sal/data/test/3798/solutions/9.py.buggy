from math import sqrt


def f(b, n):
    if n < b:
        return n
    else:
        return f(b, int(n / b)) + n % b


n = int(input())
s = int(input())

if n < s:
    print(-1)
    return
if n == s:
    print(n + 1)
    return

for b in range(2, int(sqrt(n)) + 1):
    if f(b, n) == s:
        print(b)
        return

for p in reversed(range(1, int(sqrt(n) + 1))):
    if (n - s) % p == 0:
        b = int((n - s) / p + 1)
        if f(b, n) == s:
            print(b)
            return

print(-1)
