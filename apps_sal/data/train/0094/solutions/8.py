t = int(input())

for case in range(t):
    n, T = map(int, input().split())
    a = [int(x) for x in input().split()]
    halfTticker = False
    halfT = T / 2
    white = set()

    for x in a:
        if x == halfT:
            print(int(halfTticker), end=' ')
            halfTticker = not halfTticker
        elif x in white:
            print(0, end=' ')
        elif T - x in white:
            print(1, end=' ')
        else:
            white.add(x)
            print(0, end=' ')

    print()
