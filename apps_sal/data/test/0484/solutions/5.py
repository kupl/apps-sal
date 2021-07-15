import sys


def check(a, b, x, y, q, w):
    if x + q <= a and max(y, w) <= b:
        return True
    if y + w <= b and max(x, q) <= a:
        return True
    return False


def main():
    n, a, b = list(map(int, sys.stdin.readline().split()))
    t = []
    for i in range(n):
        x, y = list(map(int, sys.stdin.readline().split()))
        if (x > a or y > b) and (x > b or y > a):
            pass
        else:
            t.append((x, y))

    ans = 0
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if check(a, b, t[i][0], t[i][1], t[j][0], t[j][1]) or check(a, b, t[i][0], t[i][1], t[j][1], t[j][0]) \
                    or check(a, b, t[i][1], t[i][0], t[j][1], t[j][0]) or check(a, b, t[i][1], t[i][0], t[j][0],
                                                                                t[j][1]):
                c = t[i][0] * t[i][1] + t[j][0] * t[j][1]
                if c > ans:
                    ans = c

    print(ans)


main()

