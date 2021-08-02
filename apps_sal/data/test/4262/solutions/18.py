N, P, Q = open(0)
*P, = map(int, P.split())
*Q, = map(int, Q.split())
def f(i): return i * f(i - 1)if i else 1


def g(l): return (l[0] - 1) * f(len(l) - 1) + g([e - 1if e > l[0]else e for e in l[1:]])if l else 0


print(abs(g(P) - g(Q)))
