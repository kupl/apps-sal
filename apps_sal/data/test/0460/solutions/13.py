import sys


def main():
    p, x, y = list(map(int, sys.stdin.readline().split()))

    s = x
    i = (s // 50) % 475
    for _ in range(25):
        i = (i * 96 + 42) % 475
        next = 26 + i
        if next == p:
            result = 0
            sys.stdout.write(str(result) + '\n')
            return

    s = x - 50
    while True:
        if s < y: break
        i = (s // 50) % 475
        for _ in range(25):
            i = (i * 96 + 42) % 475
            next = 26 + i
            if next == p:
                result = 0
                sys.stdout.write(str(result) + '\n')
                return
        s -= 50

    iplus = 1
    while True:
        for s in (x + iplus * 100, x + iplus * 100 - 50):
            i = (s // 50) % 475
            for _ in range(25):
                i = (i * 96 + 42) % 475
                next = 26 + i
                if next == p:
                    result = iplus
                    sys.stdout.write(str(result) + '\n')
                    return
        iplus += 1


main()
