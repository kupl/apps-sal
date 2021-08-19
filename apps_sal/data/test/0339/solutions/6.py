def solve(n, k, A, B):
    if k == 1:
        return A * (n - 1)
    res = 0
    while n >= k:
        res += A * (n % k)
        n -= n % k
        diff = n - n // k
        if A * diff > B:
            res += B
            n //= k
        else:
            res += A * (n - 1)
            n = 1  # finish loop
    res += A * (n - 1)
    return res


n, k, A, B = [int(input()) for i in range(4)]
print(solve(n, k, A, B))
