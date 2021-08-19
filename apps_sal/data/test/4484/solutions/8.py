(n, m) = map(int, input().split(' '))
if abs(n - m) >= 2:
    print(0)
else:
    temp = 1
    mod = 10 ** 9 + 7
    for i in range(1, min(n, m) + 1):
        temp *= i
        temp %= mod
    if n != m:
        print(temp ** 2 * max(n, m) % mod)
    else:
        print(temp ** 2 * 2 % mod)
