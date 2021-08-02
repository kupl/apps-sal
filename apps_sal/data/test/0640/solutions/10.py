from sys import stdin


def cubic():
    values = stdin.readline().split()
    a = int(values[0])
    b = int(values[1])
    awins = 0
    bwins = 0
    ties = 0
    for i in range(1, 7):
        if abs(a - i) < abs(b - i):
            awins += 1
        if abs(a - i) > abs(b - i):
            bwins += 1
        if abs(a - i) == abs(b - i):
            ties += 1
    print(awins, ties, bwins)


cubic()
