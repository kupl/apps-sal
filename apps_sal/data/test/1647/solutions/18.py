n = int(input())
a = input()
b = input()


def f(c):
    return ord(c) - 97


def g(x):
    return chr(97 + x)


fa = [i for i in range(26)]


def get_fa(x):
    return x if fa[x] == x else get_fa(fa[x])


for i in range(n):
    child = f(b[i])
    father = get_fa(child)
    while child != father:
        child = fa[child]
    fa[child] = get_fa(f(a[i]))
print(sum((i != get_fa(i) for i in range(26))))
for i in range(26):
    l = i
    r = fa[i]
    if l != r:
        print(g(l), g(r))
