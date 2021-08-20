for _ in [0] * int(input()):
    (x, y) = map(int, input().split())
    print('YNEOS'[x - y < 2::2])
