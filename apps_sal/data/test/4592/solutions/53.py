from collections import defaultdict
mod = 10**9 + 7


def factorize(n):
    out = []
    i = 2
    while 1:
        if n % i == 0:
            out.append(i)
            n //= i
        else:
            i += 1
        if n == 1:
            break
        if i > int(n**.5 + 3):
            out.append(n)
            break

    return out


N = int(input())

if N == 1:
    print(1)
    return

count = defaultdict(int)
for i in range(2, N + 1):
    f = factorize(i)
    for j in range(len(f)):
        count[f[j]] += 1

ans = 1
for k in count.keys():
    ans *= count[k] + 1 % mod

print(ans % mod)
