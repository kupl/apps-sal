n = int(input())
def f(): return ''.join(input() for i in range(n))


a, b = f(), f()
def g(k): return k // n + n * (n - 1 - k % n)
def e(k): return k
def h(k): return n * (n - 1 - k // n) + k % n
def v(k): return n * (k // n) + n - 1 - k % n


for i in (e, v, h):
    for j in [e, g, lambda k: g(g(k)), lambda k: g(g(g(k)))]:
        if all(a[k] == b[i(j(k))] for k in range(n * n)):
            (print('Yes'))
            return
print('No')
