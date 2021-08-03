def win(s, e):
    if e % 2:
        return s % 2 ^ 1
    if s > e // 2:
        return s % 2
    if s > e // 4:
        return 1

    return win(s, e // 4)


def lose(s, e):
    if s > e // 2:
        return 1

    return win(s, e // 2)


def game(n):
    res = [0, 1]
    for i in range(n):
        s, e = list(map(int, input().split()))
        res[0], res[1] = res[win(s, e)], res[lose(s, e)]

    return res


n = int(input())
print(*game(n))
