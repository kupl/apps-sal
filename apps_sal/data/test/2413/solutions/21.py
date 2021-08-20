"""
NTC here
"""
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 7)


def iin():
    return int(stdin.readline())


def lin():
    return list(map(int, stdin.readline().split()))


def main():
    for _ in range(iin()):
        n = iin()
        a = input()
        occ = []
        ch = 0
        for i in a:
            ch += 1
            if i == '1':
                occ.append(ch)
        ans = n
        if occ:
            (mx, mn) = (occ[-1], occ[0])
            ans = max(ans, max(n - mx + 1, mx) * 2, max(n - mn + 1, mn) * 2)
        print(ans)


try:
    main()
except Exception as e:
    print(e)
