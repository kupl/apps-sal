import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


q = int(input())
l = []
r = []
for i in range(q):
    ll, rr = list(map(int, input().split()))
    l.append(ll)
    r.append(rr)

dp = [0 for _ in range(10**5 + 5)]
dpsum = [0 for _ in range(10**5 + 5)]

for i in range(3, 10**5 + 1, 2):
    if is_prime(i) and is_prime((i + 1) // 2):
        # dp[i] = 1
        dpsum[i] = dpsum[i - 2] + 1
    else:
        dpsum[i] = dpsum[i - 2]

for i in range(q):
    print((dpsum[r[i]] - dpsum[l[i] - 2]))

