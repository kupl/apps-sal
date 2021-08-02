def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


n, x = map(int, input().split())
xxx = list(map(lambda xn: abs(int(xn) - x), input().split()))
ans = xxx[0]
for i in range(1, n):
    ans = gcd(ans, xxx[i])
print(ans)
