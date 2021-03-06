MOD = 1000000007
(x, y) = map(int, input().split())
if y % x == 0:
    div = y // x
    y_mult = set()
    for i in range(1, int(pow(div, 0.5) + 1)):
        if div % i == 0:
            y_mult.add(i)
            y_mult.add(div // i)
    y_mult = sorted(list(y_mult))
    ym_copy = y_mult.copy()
    for i in range(len(ym_copy)):
        ym_copy[i] = pow(2, y_mult[i] - 1, MOD)
        for j in range(i):
            if y_mult[i] % y_mult[j] == 0:
                ym_copy[i] -= ym_copy[j]
    print(ym_copy[-1] % MOD)
else:
    print(0)
