# -------------------------------------------------------------------------------
# Name:        Codeforces
# Author:      Gogol
# -------------------------------------------------------------------------------

def main():
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    s = sum(a)
    k = 0
    c = x
    while (s != 0):
        if (s > 0):
            if (abs(s) >= abs(c)):
                s = s - c
                k = k + 1
            else:
                c = c - 1
        elif (s < 0):
            if (abs(s) >= abs(c)):
                s = s + c
                k = k + 1
            else:
                c = c - 1
    print(k)


def __starting_point():
    main()


__starting_point()
