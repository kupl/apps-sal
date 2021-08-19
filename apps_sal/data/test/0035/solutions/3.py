import sys


def main():
    n, m = list(map(int, sys.stdin.readline().split()))
    if n % 3 != 0 and m % 3 != 0:
        print("NO")
        return
    f = []
    for i in range(n):
        f.append(sys.stdin.readline())

    ok = True
    if f[0][0] == f[n - 1][0]:  # vertical
        if m % 3 != 0:
            ok = False
        else:
            sz = int(m / 3)
            if f[0][0] == f[0][sz] or f[0][0] == f[0][2 * sz] or f[0][2 * sz] == f[0][sz]:
                ok = False
            else:
                for k in range(3):
                    c = f[0][k * sz]
                    for i in range(n):
                        for j in range(k * sz, (k + 1) * sz):
                            if c != f[i][j]:
                                ok = False
                                break
                        if not ok:
                            break
                    if not ok:
                        break

    else:  # horizontal
        if n % 3 != 0:
            ok = False
        else:
            sz = int(n / 3)
            if f[0][0] == f[sz][0] or f[0][0] == f[2 * sz][0] or f[2 * sz][0] == f[sz][0]:
                ok = False
            else:
                for k in range(3):
                    c = f[k * sz][0]
                    for i in range(k * sz, (k + 1) * sz):
                        for j in range(m):
                            if c != f[i][j]:
                                ok = False
                                break
                        if not ok:
                            break
                    if not ok:
                        break

    if ok:
        print("YES")
    else:
        print("NO")


main()
