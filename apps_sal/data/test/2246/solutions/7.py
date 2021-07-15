import sys


def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    x = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = list(map(int, sys.stdin.readline().split()))
        x[a - 1].append(b - 1)
        x[b - 1].append(a - 1)

    isl = [False] * n
    for i in range(1, n):
        if len(x[i]) == 1:
            isl[i] = True

    u = [False] * n
    u[0] = True
    q = [(0, 0, 1 / len(x[0]))]
    a = 0
    while len(q) != 0:
        c, s, t = q.pop()
        for i in x[c]:
            if not u[i]:
                if isl[i]:
                    a += (s + 1) * t
                else:
                    q.append((i, s + 1, t / (len(x[i])-1)))
                u[i] = True
    print(a)


main()

