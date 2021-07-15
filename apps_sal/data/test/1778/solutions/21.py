def gambling():
    n = int(input())
    aa = list(map(int, input().split()))
    bb = list(map(int, input().split()))
    aa.sort()
    bb.sort()

    sa, sb = 0, 0
    while aa or bb:
        # turn a
        if len(aa) == 0:
            bb.pop()
        elif len(bb) == 0:
            sa += aa.pop()
        elif aa[-1] >= bb[-1]:
            sa += aa.pop()
        else:
            bb.pop()

        # turn b
        if len(bb) == 0:
            aa.pop()
        elif len(aa) == 0:
            sb += bb.pop()
        elif bb[-1] >= aa[-1]:
            sb += bb.pop()
        else:
            aa.pop()

    print(sa-sb)

def __starting_point():
    gambling()
__starting_point()
