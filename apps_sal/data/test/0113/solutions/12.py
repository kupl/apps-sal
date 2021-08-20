def nok(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


(n, k) = list(map(int, input().split()))
print(nok(n, 10 ** k))
