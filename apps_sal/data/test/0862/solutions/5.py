3

def solve(N, A):
    mn = min(A)
    if mn > N:
        A = [a - (mn // N * N) for a in A]

    decr = 0
    i = 0
    while True:
        if A[i] - decr <= 0:
            return i + 1

        decr += 1
        i += 1
        if i == N:
            i = 0


def main():
    N = int(input())
    A = [int(e) for e in input().split(' ')]
    assert len(A) == N
    print(solve(N, A))


def __starting_point():
    main()

__starting_point()
