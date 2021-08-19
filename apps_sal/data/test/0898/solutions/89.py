(k, s) = list(map(int, input().split()))
p = s
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
if len(factors) == 0:
    print(1)
else:
    primes = list(factors.keys())
    exp = [0] * len(primes)
    upper = s / k
    ans = 1
    while exp[0] <= factors[primes[0]]:
        num = 1
        for i in range(len(primes)):
            num *= pow(primes[i], exp[i])
        if num == upper:
            ans = num
            break
        elif num < upper:
            ans = max(ans, num)
        index = len(primes) - 1
        done = False
        while not done:
            exp[index] += 1
            if exp[index] > factors[primes[index]]:
                if index == 0:
                    break
                else:
                    exp[index] = 0
                    index -= 1
            else:
                done = True
    print(ans)
