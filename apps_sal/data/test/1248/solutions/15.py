d1, d2, d3 = map(int, input().split())

if d1 < d2:
    s = d1
    s += min(d1 + d2, d3)
    s += min(d2, d3 + d1)
else:
    s = d2
    s += min(d1 + d2, d3)
    s += min(d1, d3 + d2)

print(s)
