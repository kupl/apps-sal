import sys


def main():
    n = int(input())
    s = list(map(int, sys.stdin.readline().split()))
    x = [i + 1 for i in range(n)]
    p1 = (0, 0)
    x0 = 0
    for z in range(2):
        for i in range(1, n):
            k = (s[i] - s[0]) / (x[i] - x[0])
            oka = True
            okp = False
            for j in range(1, n):
                if i == j:
                    continue
                c = (s[j] - s[0]) / (x[j] - x[0])
                if c != k:
                    if not okp:
                        p1 = (x[j], s[j])
                        okp = True
                    else:
                        k2 = (s[j] - p1[1]) / (x[j] - p1[0])
                        if k != k2:
                            oka = False
                            break
            if oka and okp:
                print('Yes')
                return
        (s[1], s[0]) = (s[0], s[1])
        (x[1], x[0]) = (x[0], x[1])
    print('No')


main()
