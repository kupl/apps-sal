n = int(input())


def get_p(n):
    if n == 0:
        return 0
    p = 1
    while n > 0:
        p *= n % 10
        n //= 10
    return p


mx = get_p(n)
d = 10
nn = n
while d <= n:
    nn -= d
    nn = nn - nn % d + (d - 1)
    mx = max(get_p(nn), mx)
    d *= 10
print(mx)
