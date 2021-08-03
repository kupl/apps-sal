import sys


def main():
    n = int(sys.stdin.readline())
    x = list(map(int, sys.stdin.readline().split()))
    y = [0] * n
    for i in range(n):
        y[i] = x[i] - 1

    q = []
    q.append(0)
    i = 0
    res = [-1] * n
    res[0] = 0
    while i < len(q):
        c = q[i]
        i += 1
        if c > 0 and res[c - 1] == -1:
            res[c - 1] = res[c] + 1
            q.append(c - 1)
        if c < n - 1 and res[c + 1] == -1:
            res[c + 1] = res[c] + 1
            q.append(c + 1)
        if res[y[c]] == -1:
            res[y[c]] = res[c] + 1
            q.append(y[c])

    print(' '.join(map(str, res)))


main()
