(m, s, n) = (0, set(), int(input()))
for a in map(int, input().split()):
    while a in s:
        s.remove(a)
        a += 1
    s.add(a)
    m = max(m, a)
print(m - len(s) + 1)
