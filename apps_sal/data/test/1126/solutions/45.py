def f(x, m):
    return x**2 % m


N, X, M = map(int, input().split())

A = [X]
S = {X}
i = 0
while True:
    tmp = f(A[-1], M)
    if tmp in S:
        i = A.index(tmp)
        break
    else:
        A.append(tmp)
        S.add(tmp)

n_loop = len(A) - i
s, l = A[:i], A[i:]
div, mod = divmod(N - i, n_loop)
print(sum(s) + sum(l) * div + sum(l[:mod]))
