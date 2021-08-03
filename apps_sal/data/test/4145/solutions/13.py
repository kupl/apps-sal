x = int(input())
if x == 2:
    print((2))
    return
while True:
    flg = 0
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            flg += 1
        if i == int(x**0.5) and flg == 0:
            print(x)
            return
    x += 1
