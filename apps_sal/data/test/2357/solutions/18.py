"""
NTC here
"""
from sys import stdin


def iin(): return int(stdin.readline())


def lin(): return list(map(int, stdin.readline().split()))


# range = xrange
# input = raw_input


def main():
    t = iin()
    while t:
        t -= 1
        n = iin()
        a = lin()
        d = {}
        for i in range(n):
            try:
                d[a[i]].append(i)
            except:
                d[a[i]] = [i]
        ans = -1
        for i in d:
            l = len(d[i])
            for j in range(l - 1):
                if ans == -1:
                    ans = d[i][j + 1] - d[i][j] + 1
                else:
                    ans = min(d[i][j + 1] - d[i][j] + 1, ans)
        print(ans)


main()
# try:
#     main()
# except Exception as e: print(e)
