def start(x, cnt):
    nonlocal ans
    i = x
    res = 0
    while i <= n:
        res += n // i
        i *= x
    ans = min(ans, res // cnt)

n, b = map(int, input().split())
nb = b
ans = 1e20
i = 2
while i * i <= b:
    if nb % i == 0:
        cnt = 0
        while nb % i == 0:
            cnt += 1
            nb //= i
        start(i, cnt)
    i += 1
if nb > 1:
    start(nb, 1)
print(ans)
