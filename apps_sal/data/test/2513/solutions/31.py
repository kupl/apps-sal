import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input()
    L = ["S", "W"]

    for first in L:
        for second in L:
            res = ["" for _ in range(n)]
            res[0] = first
            res[1] = second
            for i in range(1, n - 1):
                if s[i] == "o":
                    if res[i] == "S" and res[i - 1] == "S":
                        res[i + 1] = "S"
                    elif res[i] == "S" and res[i - 1] == "W":
                        res[i + 1] = "W"
                    elif res[i] == "W" and res[i - 1] == "W":
                        res[i + 1] = "S"
                    else:
                        res[i + 1] = "W"
                else:
                    if res[i] == "S" and res[i - 1] == "S":
                        res[i + 1] = "W"
                    elif res[i] == "S" and res[i - 1] == "W":
                        res[i + 1] = "S"
                    elif res[i] == "W" and res[i - 1] == "W":
                        res[i + 1] = "W"
                    else:
                        res[i + 1] = "S"

            if s[-1] == "o":
                if (res[-1] == "S" and res[-2] != res[0]) or (res[-1] == "W" and res[-2] == res[0]):
                    continue
            else:
                if (res[-1] == "S" and res[-2] == res[0]) or (res[-1] == "W" and res[-2] != res[0]):
                    continue

            if s[0] == "o":
                if (res[0] == "S" and res[-1] != res[1]) or (res[0] == "W" and res[-1] == res[1]):
                    continue
            else:
                if (res[0] == "S" and res[-1] == res[1]) or (res[0] == "W" and res[-1] != res[1]):
                    continue

            print(("".join(res)))
            break
        else:
            continue
        break
    else:
        print((-1))


def __starting_point():
    resolve()

__starting_point()
