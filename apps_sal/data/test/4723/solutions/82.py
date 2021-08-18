import sys

stdin = sys.stdin
sys.setrecursionlimit(10 ** 7)
MIN = -10 ** 9
MOD = 10 ** 9 + 7
INF = float("inf")
IINF = 10 ** 18


def solve():
    s = str(stdin.readline().rstrip())
    t = str(stdin.readline().rstrip())
    anss = []
    for i in range(len(s) - len(t) + 1):
        test = s[i:len(t) + i]
        flag = True
        for j in range(len(t)):
            if test[j] != "?" and test[j] != t[j]:
                flag = False
        if flag == True:
            ans = s[0:i] + t + s[i + len(t):]
            ans = ans.replace("?", "a")
            anss.append(ans)
    if len(anss) == 0:
        print("UNRESTORABLE")
        return
    anss.sort()
    print((anss[0]))


def __starting_point():
    solve()


__starting_point()
