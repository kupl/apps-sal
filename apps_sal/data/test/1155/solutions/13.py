def r(): return list(map(int, input().split()))


n, m = r()
def check(x): return x[0] / x[1]


print(min(check(r()) for x in range(n)) * m)
