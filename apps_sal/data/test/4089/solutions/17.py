N = int(input())

ans = ''

while True:
    n = int(N / 26)
    r = N % 26

    if r == 0:
        r = 26
        n -= 1

    ans = chr(96 + r) + ans
    if n == 0:
        break
    else:
        N = n

print(ans)
