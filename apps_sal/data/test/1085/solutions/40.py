N = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


ans = [2]
if N not in ans:
    ans.append(N)
if N % (N - 1) != 0 and N - 1 not in ans:
    ans.append(N - 1)
D = make_divisors(N)
for d in D:
    now = N
    if d == 1:
        continue
    while now % d == 0:
        now = now // d
    if now % d == 1:
        if d not in ans:
            ans.append(d)
ans2 = []
for a in ans:
    i = 1
    while a ** i <= N:
        x = a ** i
        now = N
        while now % x == 0:
            now = now // x
        if now % x == 1:
            if x not in ans2:
                ans2.append(x)
        i += 1
d2 = make_divisors(N - 1)
for d in d2:
    if d != 1 and d not in ans2:
        ans2.append(d)
print(len(ans2))
