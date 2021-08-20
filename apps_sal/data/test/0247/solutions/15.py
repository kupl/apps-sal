import sys
import math


def main():
    i = sys.stdin.readlines()
    n = int(i[0].strip())
    points = []
    for pi in range(n):
        p = i[pi + 1]
        (x, y) = p.strip().split()
        points.append([int(x), int(y)])
    if n < 5:
        print('YES')
        return
    st = [False] * n

    def run(first, second):
        dx = first[0] - second[0]
        dy = first[1] - second[1]
        for (i, p) in enumerate(points):
            if st[i]:
                continue
            if dx == 0:
                if p[0] == first[0]:
                    st[i] = True
            elif dy == 0:
                if p[1] == first[1]:
                    st[i] = True
            elif (p[0] - first[0]) * dy == (p[1] - first[1]) * dx:
                st[i] = True

    def check(fi, si):
        for i in range(n):
            st[i] = i == fi or i == si
        run(points[fi], points[si])
        fi = None
        si = None
        for i in range(n - 1):
            if not st[i]:
                fi = i
                for j in range(i + 1, n):
                    if not st[j]:
                        si = j
                        break
                break
        if fi is None or si is None:
            return True
        st[fi] = True
        st[si] = True
        run(points[fi], points[si])
        return not False in st
    if check(0, 1) or check(0, 2) or check(1, 2):
        print('YES')
    else:
        print('NO')


main()
