def mina():
    a, b, c = map(int, input().split())
    k = 0
    while k * a <= c:
        if (c - k * a) % b == 0:
            print("Yes")
            return
        k += 1
    print("No")


mina()
