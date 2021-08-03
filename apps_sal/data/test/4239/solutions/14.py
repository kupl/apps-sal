def cal(n, x):
    res = 0
    while n > 0:
        res += n % x
        n //= x
    return res


N = int(input())

ans = N
for i in range(N + 1):
    ans = min(ans, cal(i, 6) + cal(N - i, 9))
print(ans)
