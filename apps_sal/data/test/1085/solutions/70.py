N = int(input())


def divisors(n):
    ret1 = []
    ret2 = []
    i = 1
    while i**2 <= N:
        if n % i == 0:
            ret1 += [i]
            ret2 += [n // i]
        i += 1
    return ret1 + ret2


ans1 = set(divisors(N - 1))
ans2_cand = set(divisors(N))
ans2 = 0
for k in ans2_cand:
    if k == 1:
        continue
    n = N
    while n % k == 0:
        n = n // k
    if n % k == 1:
        ans2 += 1


print(len(ans1) + ans2 - 1)
