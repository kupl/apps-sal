(a, b, c, d) = map(int, input().split())
e = []
f = a * b
g = c * d
e.append(f)
e.append(g)
if f == g:
    print(f)
else:
    print(max(e))
