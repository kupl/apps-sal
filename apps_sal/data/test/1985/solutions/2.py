import sys


def main():
    (k, n) = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    for i in range(1, k):
        a[i] = a[i - 1] + a[i]
    c = set()
    for i in range(k):
        x = b[0] - a[i]
        u = {}
        for j in range(k):
            u[x + a[j]] = True
        flag = True
        for j in range(n):
            if b[j] not in u:
                flag = False
                break
        if flag:
            c.add(x)
    print(len(c))


main()
