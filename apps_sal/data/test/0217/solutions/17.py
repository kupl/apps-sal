def main():
    a, b, f, k = list(map(int, input().split()))
    fuels = 0
    trips = 0
    pos = 0
    move = 1
    gas = b

    while trips < k:
        if gas < 0:
            print(-1)
            return
        if move == 1:
            if pos == 0:
                pos = f
                gas -= f
            elif pos == f:
                needed_gas = (a - f) if trips == k - 1 else 2 * (a - f)
                if gas < needed_gas:
                    gas = b
                    fuels += 1
                gas -= (a - f)
                pos = a
            elif pos == a:
                trips += 1
                if trips == k:
                    break
                move = -1
        elif move == -1:
            if pos == 0:
                trips += 1
                if trips == k:
                    break
                move = 1
            elif pos == f:
                needed_gas = f if trips == k - 1 else 2 * f
                if gas < needed_gas:
                    gas = b
                    fuels += 1
                pos = 0
                gas -= f
            elif pos == a:
                pos = f
                gas -= (a - f)

    print(fuels)

main()

