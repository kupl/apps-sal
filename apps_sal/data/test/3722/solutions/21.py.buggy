import sys
input = sys.stdin.readline

n = int(input())
caa = input().rstrip()
cab = input().rstrip()
cba = input().rstrip()
cbb = input().rstrip()

INF = 10**9 + 7


def modinv(a, m):
    b = m
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while not b == 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return lastx % m


if n == 2:
    print(1)
    return

if cab == 'A' and caa == 'A':
    ans = 1

if cab == 'B' and cbb == 'B':
    ans = 1

if cab == 'A' and caa == 'B':
    if cba == 'B':
        ans = pow(2, n - 3, INF)

    else:
        ans = 0
        x = 0
        c = 1
        while n - 2 - x >= x:
            ans = (ans + c) % INF
            c = c * (n - 3 - 2 * x) * (n - 2 - 2 * x) * modinv(x + 1, INF) * modinv(n - 2 - x, INF)
            c = c % INF
            x += 1

if cab == 'B' and cbb == 'A':
    if cba == 'A':
        ans = pow(2, n - 3, INF)

    else:
        ans = 0
        x = 0
        c = 1
        while n - 2 - x >= x:
            ans = (ans + c) % INF
            c = c * (n - 3 - 2 * x) * (n - 2 - 2 * x) * modinv(x + 1, INF) * modinv(n - 2 - x, INF)
            c = c % INF
            x += 1

print(ans)
