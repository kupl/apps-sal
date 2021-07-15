import sys


def main():
    n, k = list(map(int, sys.stdin.readline().split()))
    x = list(map(int, sys.stdin.readline().split()))
    ch = n
    dv = 2 * n

    for i in range(k):
        if x[i] % 4 == 2 and dv > 0:
            x[i] -= 2
            dv -= 1
    for i in range(k):
        while x[i] > 3 and ch > 0:
            x[i] -= 4
            ch -= 1

    for i in range(k):
        if x[i] % 4 == 1 and dv > 0:
            x[i] -= 1
            dv -= 1

    for i in range(k):
        while x[i] >= 3 and ch > 0:
            x[i] -= 4
            ch -= 1
    p1 = 0
    p2 = 0
    for i in range(k):
        if x[i] == 2:
            if p2 > 0:
                p2 -= 1
                x[i] = 0
            elif ch > 0:
                x[i] = 0
                p1 += 1
                ch -= 1
            elif p1 > 1:
                p1 -= 2
                x[i] = 0
        elif x[i] == 1:
            if p1 > 0:
                p1 -= 1
                x[i] = 0
            elif ch > 0:
                p2 += 1
                x[i] = 0
                ch -= 1
            elif p2 > 0:
                p2 -= 1
                x[i] = 0

        while x[i] > 0 and dv > 0:
            x[i] -= 2
            dv -= 1

    ok = True
    for i in range(k):
        if x[i] > 0:
            ok = False
            break

    if ok:
        print("YES")
    else:
        print("NO")


main()

