def f_max(X, digit):
    if X == 0:
        return sum([Ad[i] * 2 ** i for i in range(digit)])
    elif X == 2 ** digit - 1:
        return sum([max(Ad[i], N - Ad[i]) * 2 ** i for i in range(digit)])
    elif X >= 2 ** (digit - 1):
        return max((N - Ad[digit - 1]) * 2 ** (digit - 1) + f_max(X - 2 ** (digit - 1), digit - 1), Ad[digit - 1] * 2 ** (digit - 1) + f_max(2 ** (digit - 1) - 1, digit - 1))
    else:
        return Ad[digit - 1] * 2 ** (digit - 1) + f_max(X, digit - 1)


(N, K) = map(int, input().split())
(K_max, digits) = (2 * 10 ** 12, 0)
while K_max > 0:
    K_max >>= 1
    digits += 1
Ad = [0] * digits
for a in list(map(int, input().split())):
    for i in range(digits):
        Ad[i] += a % 2
        a >>= 1
print(f_max(K, digits))
