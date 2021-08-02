def nok(a, b):
    c = a * b
    while (a != 0) and (b != 0):
        if a > b: a %= b;
        else: b %= a;
    return c // (a + b);


nk = input().split()
n, k = int(nk[0]), int(nk[1])
print(nok(10**k, n))
