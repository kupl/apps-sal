N = int(input())
T = [int(input()) for _ in range(N)]


def gcd(a, b):
    l = max(a, b)
    s = min(a, b)
    while True:
        x = s
        y = l % s
        if y == 0:
            break
        else:
            l = x
            s = y
    return s


if N != 1:
    ans = T[0] * T[1] // gcd(T[0], T[1])
    for n in range(1, N):
        ans = ans * T[n] // gcd(ans, T[n])
else:
    ans = T[0]

print(ans)
