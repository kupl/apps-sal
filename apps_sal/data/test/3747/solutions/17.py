d = {}
for i in input().strip():
    d[i] = d.get(i, 0) + 1
ans = min(d.get('B', 0), d.get('u', 0) // 2, d.get('l', 0), d.get('b', 0), d.get('a', 0) // 2, d.get('s', 0), d.get('r', 0))
print(ans)
