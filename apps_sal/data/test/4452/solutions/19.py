def sol():
    x = int(input())
    res = []
    pw = 0
    while x > 0:
        p = x % 10
        if p > 0:
            d = p * 10 ** pw
            res.append(d)
        pw += 1
        x //= 10
    print(len(res))
    print(*res)


for n in range(int(input())):
    sol()
