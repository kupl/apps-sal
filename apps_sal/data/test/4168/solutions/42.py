import math
import sys
pin = sys.stdin.readline


def main():
    N = int(pin())
    ansl = []
    if N == 0:
        print(0)
        return
    while True:
        if N == 0:
            break
        ansl.append(N % 2)
        N = -(N // 2)
    ans = ''.join(map(str, ansl))
    ans = ans[::-1]
    print(ans)
    return


main()
