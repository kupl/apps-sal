def nld(n):
    val = 0
    while n > 0:
        if n % 10 in (4, 7):
            val += 1
        n //= 10
    return val

n, k = (int(x) for x in input().split())
print(sum(1 for x in (int(x) for x in input().split()) if nld(x) <= k))
