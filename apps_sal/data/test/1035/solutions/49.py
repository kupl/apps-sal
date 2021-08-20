(a, b) = list(map(int, input().split()))


def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)


p = gcd(a, b)
factors = {}
while p > 1:
    f = False
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            p //= i
            f = True
            break
    if not f:
        if p in factors:
            factors[p] += 1
        else:
            factors[p] = 1
        break
print(len(factors) + 1)
