n = int(input())
m = n

digits = 0
while m > 0:
    m //= 10
    digits += 1
if n < 5:
    print(n * (n - 1) // 2)
    return
if n == 10 ** digits - 1:
    print(n // 2)
    return
if n >= 5 * 10 ** (digits - 1):
    print(n - 5 * 10 ** (digits - 1) + 1)
else:
    fst = int(str(n)[0])
    res = (fst) * (fst - 1) // 2 * 10 ** (digits - 1)
    res += (fst) * (10 ** (digits - 1) // 2 - 1)

    n = int(str(n)[1:])
    digits -= 1
    if n == 10 ** digits - 1:
        res += (n // 2)
    elif n >= 5 * 10 ** (digits - 1):
        res += (n - 5 * 10 ** (digits - 1) + 1)
    res += (n + 1) * fst
    print(res)
