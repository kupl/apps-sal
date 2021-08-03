n, k = list(map(int, input().split()))
def g(x): return int(x) % k


a = list(map(g, input().split()))


def nod(a, b):
    while b > 0:
        a %= b
        a, b = b, a
    return a


c = k
for x in a:
    if x != 0:
        c = nod(c, x)
print(k // c)
print(' '.join(map(str, list(range(0, k, c)))))
