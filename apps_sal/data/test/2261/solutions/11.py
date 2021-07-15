def f(k):
    if(k == '+'):
        return '*'
    else:
        return '+'

def g(k):
    s = []
    for c in k:
        s.append(f(c))
    return ''.join(s)


def solve(k):
    if(k == 0):
        return ['+']
    else:
        h = solve(k - 1)
        n = 1 << k
        q = n >> 1
        for i in range(q):
            h.append(h[i] + g(h[i]))
            h[i] += h[i]
        return h

k = int(input())
h = solve(k)
for a in h:
    print(a)
