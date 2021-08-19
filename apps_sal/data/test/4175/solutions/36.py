import sys
input = sys.stdin.readline


def main():
    N = int(input())
    W = [input().strip() for _ in range(N)]
    s = set()
    prev = ''
    for w in W:
        if w in s:
            print('No')
            return
        if prev == '':
            prev = w[-1]
        elif prev == w[0]:
            prev = w[-1]
        else:
            print('No')
            return
        s.add(w)
    print('Yes')


def __starting_point():
    main()


__starting_point()
