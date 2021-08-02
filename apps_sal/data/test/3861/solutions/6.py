def isqrt(n):
    if n < 0:
        return None
    elif 0 <= n <= 1:
        return n
    x = n // 2
    seen = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen:
            return None
        seen.add(x)
    return x


def is_square(n):
    return isqrt(n) is not None


n = int(input())
a = [int(v) for v in input().split()]

print(max(v for v in a if not is_square(v)))
