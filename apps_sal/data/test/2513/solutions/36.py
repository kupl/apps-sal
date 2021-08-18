
N = int(input())
s = input()

d = {"S": "W", "W": "S"}


def f(x, y, i, j):
    if y == "S":
        if s[j] == "o":
            return x
        else:
            return d[x]
    else:
        if s[j] == "o":
            return d[x]
        else:
            return x


def solve(t):
    l = [None] * N
    l[0], l[1] = t
    l[-1] = f(l[1], l[0], 1, 0)
    for i in range(2, N - 1):
        l[i] = f(l[i - 2], l[i - 1], i - 2, i - 1)
    x = f(l[-3], l[-2], -3, -2)
    y = f(l[-2], l[-1], -2, -1)
    if x == l[-1] and y == l[0]:
        return l
    else:
        return None


def main():
    l = [("S", "S"), ("S", "W"), ("W", "S"), ("W", "W")]
    ans = None
    for t in l:
        ans = solve(t)
        if ans is not None:
            break
    if ans is None:
        print((-1))
    else:
        print(("".join(ans)))


def __starting_point():
    main()


__starting_point()
