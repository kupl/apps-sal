a, b = input(), input()
n = len(b)
def f(a, b):
    i, t = 0, [0]
    for q in a:
        if i < n and q == b[i]: i += 1
        t.append(i)
    return t
u, v = f(a, b), f(a[::-1], b[::-1])[::-1]
t = [x + y for x, y in zip(u, v)]
i = t.index(max(t))
x, y = u[i], v[i]
s = b[:x] + b[max(x, n - y):]
print(s if s else '-')
