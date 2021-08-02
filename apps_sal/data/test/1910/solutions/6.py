ans = 0

n = int(input())

for i in range(1, n):
    p = 2 * n - 2 - i - n + 1
    q = i - 1

    if p >= 1:
        p = 3 * (4**(p - 1))
    else:
        p = 1

    if q >= 1:
        q = 3 * (4**(q - 1))
    else:
        q = 1

    ans += 4 * p * q

print(ans)
