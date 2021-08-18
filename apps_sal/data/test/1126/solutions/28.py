

def solve(*args: str) -> str:
    n, x, m = list(map(int, args[0].split()))

    a = x
    ret = 0
    I = [-1] * (m + 1)
    A = []

    for i in range(n):
        if I[a] < 0:
            I[a] = i
            A.append(a)
            ret += a
        else:
            A = A[I[a]:]
            d, r = divmod(n - i - 1, len(A))
            ret += (d + 1) * sum(A[:r + 1]) + d * sum(A[r + 1:])
            break
        a = pow(a, 2, m)

    return str(ret)


def __starting_point():
    print((solve(*(open(0).read().splitlines()))))


__starting_point()
