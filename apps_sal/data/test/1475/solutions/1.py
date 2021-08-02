def g(b, w):
    if(b, w) in x:
        return x[(b, w)]
    x[(b, w)] = sum(c[i]for i in r(len(c))if i % m == w)if b == 1else sum(g(b // 2, l) * g(b - b // 2, (w - (l * pow(10, b - b // 2, m)) % m + m) % m)for l in r(m)) % (10**9 + 7)
    return x[(b, w)]


q, r = input, range
n, b, w, m = map(int, q().split())
a, x = list(map(int, q().split())), {}
c = [a.count(i)for i in r(10)]
print(g(b, w))
