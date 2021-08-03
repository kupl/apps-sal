def enum_divisors(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
    return res


N = int(input())
divs = enum_divisors(N)
ans = float("inf")
for d in divs:
    ans = min(ans, (d - 1) + (N // d - 1))
print(ans)
