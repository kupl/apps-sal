def iroha():
    a, b = input().split()
    exmap = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    aa = exmap[a]
    bb = exmap[b]
    if aa < bb:
        print("<")
    elif aa > bb:
        print(">")
    else:
        print("=")


def __starting_point():
    iroha()


__starting_point()
