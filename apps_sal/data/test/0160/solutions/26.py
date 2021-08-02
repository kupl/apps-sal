n, k = map(int, input().split())
A = list(map(int, input().split()))
s = sum(A)


def md(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort(reverse=True)
    return divisors


P = md(s)


def test(x):
    L = sorted([a % x for a in A])
    M = sum(L)
    c = M // x
    for _ in range(c):
        M -= L.pop()
    return M <= k


for p in P:
    if test(p):
        print(p)
        break
