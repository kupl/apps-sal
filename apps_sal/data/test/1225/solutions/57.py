H = int(input())


def battle(h):
    if h == 1:
        return 1
    else:
        return 2 * battle(h // 2) + 1


print(battle(H))
