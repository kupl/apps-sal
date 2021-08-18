def solve(a, b):
    assert 1 <= a and 1 <= b
    if a == 1 and b == 1:
        return 1
    else:
        a, b = max(a, b), min(a, b)
        p, q = a // b, a % b
        if q == 0:
            p, q = p - 1, 1
        return p + solve(q, b)


a, b = list(map(int, input().split()))
print(solve(a, b))
