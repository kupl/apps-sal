
X = int(input())

if X == 1:
    print((1))
    return


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


while True:
    a = prime_factorize(X)
    temp = []
    c = 1
    sw = True
    if len(a) == 1:
        sw = False
    for i in range(len(a) - 1):
        if a[i] != a[i + 1]:
            temp.append(c)
            c = 0
        c += 1
    temp.append(c)

    for j in range(len(temp) - 1):
        if temp[j] != temp[j + 1] or temp[j] == 1:
            sw = False
    if sw == True:
        print(X)
        return
    X -= 1
