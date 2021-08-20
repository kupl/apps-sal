(A, B, C, D) = (lambda: map(int, input().split()), range, min, max)
(n, q) = A()
(a, b) = ([n] * n, [n] * n)
(h, w) = (n, n)
E = (n - 2) ** 2
for _ in B(q):
    (Q, x) = A()
    if Q - 1:
        for i in B(x, D(x, h)):
            b[i - 1] = w
        h = C(h, x)
        E -= b[x - 1] - 2
    else:
        for i in B(x, D(x, w)):
            a[i - 1] = h
        w = C(w, x)
        E -= a[x - 1] - 2
print(E)
