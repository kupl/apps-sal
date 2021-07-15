s = input()
t = input()
if set(t) & set(s) == set(t):
    n = -1
    c = 0
    for i in t:
        n = s.find(i, n + 1)
        if n == -1:
            c += 1
            n = s.find(i)
    print(n + len(s) * c + 1)
else:
    print(-1)
