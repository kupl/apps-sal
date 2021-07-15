import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return list(map(int, stdin.readline().split()))
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    C = []
    S = []
    F = []
    for i in range(n - 1):
        c, s, f = nm()
        C.append(c)
        S.append(s)
        F.append(f)
    for i in range(n - 1):
        time = 0
        for j in range(i, n - 1):
            if time <= S[j]:
                time = S[j] + C[j]
            else:
                time = time + (F[j] - (time - S[j]) % F[j]) % F[j] + C[j]
        print(time)
    print((0))


def __starting_point():
    main()

__starting_point()
