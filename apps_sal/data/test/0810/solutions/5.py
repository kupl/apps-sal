(a, b, n) = list(map(int, input().split()))


def ok(s):
    while s:
        if s % 10 != a and s % 10 != b:
            return False
        s = int(s / 10)
    return True


ans = 0
p = int(1000000000.0 + 7)
A = [1]
for i in range(1, n + 1):
    A.append(int(i * A[i - 1] % p))
for x in range(0, n + 1):
    y = n - x
    if ok(a * x + b * y):
        ans += A[n] * pow(A[x], p - 2, p) % p * pow(A[y], p - 2, p) % p
        ans %= p
print(int(ans))
