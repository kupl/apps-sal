def read():
    return map(int, input().split())


(n, f) = read()
p = [tuple(read()) for i in range(n)]
d = [min(2 * k, l) - min(k, l) for (k, l) in p]
d.sort(reverse=1)
ans = sum((min(k, l) for (k, l) in p)) + sum(d[:f])
print(ans)
