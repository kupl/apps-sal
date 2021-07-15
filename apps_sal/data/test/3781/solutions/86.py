sc = map(int, open(0).read().split())
ni = lambda: next(sc)

T = ni()
for _ in range(T):
    N = ni()
    A = sorted(ni() for _ in range(N))

    if N % 2 == 0 and A[::2] != A[1::2]:
        print("First")
    else:
        print("Second")
