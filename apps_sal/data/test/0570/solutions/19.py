a, b = list(map(int, input().split()))

turn = True
now = 1
while True:
    if turn:
        if a < now:
            print("Vladik")
            return
        else:
            a -= now
    else:
        if b < now:
            print("Valera")
            return
        else:
            b -= now
    now += 1
    turn = not turn
