import math


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    return divisors


n, a, b = list(map(int, input().split()))
ans = []
if(n < a + b - 1 or n > a * b):
    print(-1)
else:
    if(b >= 2):
        x = (n - a) // (b - 1)
        y = (n - a) % (b - 1)
    else:
        x = 1
        y = 1
    times = [0 for i in range(b - 1)]
    for i in range(a):
        ans.append(n - a + i + 1)
    for i in range(b - 1):
        if(i < y):
            times[i] = x + 1
        else:
            times[i] = x
    now = n - a
    for i in range(b - 1):
        now -= times[i]
        for j in range(times[i]):
            ans.append(now + j + 1)
print(' '.join(map(str, ans)))
