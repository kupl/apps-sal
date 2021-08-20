import sys


def main():
    n = int(sys.stdin.readline())
    w = sys.stdin.readline().split()
    w = [(int(w[i]), i) for i in range(n)]
    p = [i for i in sys.stdin.readline().strip()]
    w.sort()
    res = []
    (intro, extro) = (0, [])
    for pa in p:
        if pa == '0':
            extro.append(w[intro][1])
            res.append(str(w[intro][1] + 1))
            intro += 1
        else:
            s = extro.pop()
            res.append(str(s + 1))
    print(' '.join(res))


main()
