import sys
input = sys.stdin.readline

S = list(input().rstrip())
L = len(S)
Q = int(input())
data = []
for _ in range(Q):
    A = list(map(str, input().split()))
    data.append(A)

alp = [chr(i) for i in range(97, 97 + 26)]
BITs = {}
for a in alp:
    BITs[a] = [0] * (L + 1)


def query_sum(i, al):
    s = 0
    while i > 0:
        s += BITs[al][i]
        i -= i & -i
    return s


def add(i, x, al):
    while i <= L:
        BITs[al][i] += x
        i += i & -i


def main():
    for i, s in enumerate(S):
        add(i + 1, 1, s)

    for A in data:
        if A[0] == '1':
            l, s = int(A[1]), A[2]
            for al in alp:
                if query_sum(l, al) - query_sum(l - 1, al) == 1:
                    add(l, -1, al)
                    break
            add(l, 1, s)
        else:
            l, r = int(A[1]), int(A[2])
            c = 0
            for al in alp:
                if query_sum(r, al) - query_sum(l - 1, al) > 0:
                    c += 1
            print(c)


def __starting_point():
    main()


__starting_point()
