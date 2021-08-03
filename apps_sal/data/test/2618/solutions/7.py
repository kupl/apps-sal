def gcd(a, b):
    if a * b == 0:
        return a + b
    return gcd(b, a % b)


def f():
    n = int(input())
    p = list([int(x) // 100 for x in input().split()])
    x, a = list(map(int, input().split()))
    y, b = list(map(int, input().split()))
    k = int(input())
    p.sort(reverse=True)
    ps = [0]
    for i in range(0, n):
        ps.append(ps[-1] + p[i])
    i = 0
    j = n
    if x < y:
        x, y, a, b = y, x, b, a
    m = n
    ab = a * b // gcd(a, b)
    colab = m // ab
    cola = m // a - colab
    colb = m // b - colab
    res = (ps[colab] * (x + y) + (ps[colab + cola] - ps[colab]) * x
           + (ps[colab + cola + colb] - ps[cola + colab])*y)
    if res < k:
        return -1
#    print(p, ps, cola, colb, colab, k, res, ps[colab]*(x+y), (ps[colab + cola] - ps[colab])*x, (ps[colab+cola+colb] - ps[colab+cola])*y)
    while j - i > 1:
        m = (i + j) // 2
        colab = m // ab
        cola = m // a - colab
        colb = m // b - colab
        res = (ps[colab] * (x + y) + (ps[colab + cola] - ps[colab]) * x
               + (ps[colab + cola + colb] - ps[cola + colab])*y)
        if res >= k:
            j = m
        else:
            i = m
    return j


for i in range(int(input())):
    print(f())
