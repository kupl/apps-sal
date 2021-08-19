def R():
    return map(int, input().split())


(n, k) = R()
b = list(R())


def solve(n, k, b):
    m = [n % b[i] for i in range(k)]
    from operator import itemgetter
    i = min(enumerate(m), key=itemgetter(1))[0]
    return (i, n // b[i])


t = solve(n, k, b)
print(t[0] + 1, t[1])
