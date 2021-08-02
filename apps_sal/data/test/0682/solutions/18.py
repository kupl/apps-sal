def sign(num):
    return -1 if num < 0 else 1


def rook(cord):
    if cord[0] == cord[2] and cord[1] == cord[3]:
        return 0
    if cord[0] == cord[2] or cord[1] == cord[3]:
        return 1
    return 2


def bishop(cord):
    if (cord[0] + cord[1]) % 2 != (cord[2] + cord[3]) % 2:
        return 0
    elif (cord[0] - cord[1] == cord[2] - cord[3]) or (cord[0] + cord[1] == cord[2] + cord[3]):
        return 1
    return 2


def king(cord):
    return max(abs(cord[0] - cord[2]), abs(cord[1] - cord[3]))


cord = list(map(int, input().split()))
print(rook(cord), bishop(cord), king(cord))
