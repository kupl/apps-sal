from functools import reduce


def factors(n):
    from functools import reduce
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


for _ in range(int(input().strip())):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    num = max(arr) * min(arr)
    s1 = set(arr)
    s1.add(1)
    s1.add(num)
    s2 = factors(num)
    if s1 == s2:
        print(num)
    else:
        print(-1)
