n, b = [int(x) for x in input().split()]
i = 2
ans = -1


def update(p):
    cnt = 0
    tmp = p
    while tmp <= n:
        cnt += n // tmp
        tmp *= p
    return cnt


while i * i <= b:
    if b % i == 0:
        q = 0
        while b % i == 0:
            b //= i
            q += 1
        cnt = update(i)
        if ans == -1:
            ans = cnt // q
        else:
            ans = min(ans, cnt // q)
    i += 1
if b > 1:
    cnt = update(b)
    if ans == -1:
        ans = cnt
    else:
        ans = min(ans, cnt)
print(ans)
