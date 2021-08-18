"""
NTC here
"""
from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def iin(): return int(stdin.readline())


def lin(): return list(map(int, stdin.readline().split()))


MAX_INT = 99999999


def p3(a):
    ans = []
    while a:
        ans.append(a % 3)
        a //= 3
    return ans


def main():
    t = iin()
    while t:
        t -= 1
        n = iin()
        pw = p3(n) + [0, 0]
        l = len(pw)
        ch = 1
        for i in range(l - 3, -1, -1):
            if pw[i] > 1:
                if ch:
                    pw[i] = 0
                    pw[i + 1] += 1
                    ch = 0
                else:
                    pw[i] = 0
            if ch == 0:
                pw[i] = 0
        for i in range(l - 1):
            if pw[i] > 1:
                pw[i] = 0
                pw[i + 1] += 1
        ans = 0
        pw = pw[::-1]
        for i in pw:
            ans = ans * 3 + i
        print(ans)


main()
