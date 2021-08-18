

def main():
    n_rooms = int(input())
    line = input()
    keys = line[0::2]
    doors = line[1::2]
    buykeys = 0
    keyinbag = {}
    for room_index in range(n_rooms - 1):
        if keys[room_index] in keyinbag:
            keyinbag[keys[room_index]] += 1
        else:
            keyinbag[keys[room_index]] = 1
        if not doors[room_index].lower() in keyinbag or\
           keyinbag[doors[room_index].lower()] < 1:
            buykeys += 1
        else:
            keyinbag[doors[room_index].lower()] -= 1
    print(buykeys)


def __starting_point():
    main()


__starting_point()
