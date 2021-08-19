def enum_divisors(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n // i)
    return res


(N, M) = list(map(int, input().split()))
divs = sorted(enum_divisors(M), reverse=True)
ans = max((d for d in divs if M // d >= N))
print(ans)
