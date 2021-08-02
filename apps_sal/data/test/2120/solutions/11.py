R = lambda: map(int, input().split())
n, m = R()
v = [0] + list(R())
print(sum(min(v[x], v[y]) for x, y in (R() for i in range(m))))
