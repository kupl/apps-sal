from sys import stdin
rs = lambda : stdin.readline().strip()
ri = lambda : int(rs())
ril = lambda : list(map(int, rs().split()))

def main():
    N = ri()
    a = ril()
    print((max(a) - min(a)))


def __starting_point():
    main()

__starting_point()
