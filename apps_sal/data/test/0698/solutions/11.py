# -------------------------------------------------------------------------------
# Name:        Codeforces
# Author:      Gogol
# -------------------------------------------------------------------------------

def main():
    x, k = list(map(int, input().split()))
    a = x * [0]
    t = k
    ans1 = ans2 = 0
    ans = 0
    while (t > 0):
        c = list(map(int, input().split()))
        if (len(c) == 2):
            a[c[1]] = 1
        else:
            a[c[1]] = 1
            a[c[2]] = 1
        t = t - 1
    t = 1
    while (t <= x - 1):
        if (a[t] != 1):
            ans2 = ans2 + 1
        t = t + 1
    t = 1
    n = x - 1 - 1
    while (t <= n and n > 2):
        if (a[t] == 0 and a[t + 1] == 0):
            a[t] = 1
            a[t + 1] = 1
            ans1 = ans1 + 1
            t = t + 2
        else:
            t = t + 1
    t = 1
    while (t <= x - 1):
        if (a[t] == 0):
            ans1 = ans1 + 1
        t = t + 1
    print(ans1, ans2)


def __starting_point():
    main()


__starting_point()
