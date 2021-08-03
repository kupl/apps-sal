def solve():
    S = input()
    counter = 97
    res = ""
    for s in list(S):
        s = ord(s)
        if counter >= 123:
            res += chr(s)
            continue

        if s <= counter:
            res += chr(counter)
            counter += 1
        else:
            res += chr(s)

    if counter == 123:
        print(res)
    else:
        print(-1)


def __starting_point():
    solve()


__starting_point()
