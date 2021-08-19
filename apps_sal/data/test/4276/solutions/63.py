(n, t) = map(int, input().split())
cl = []
for i in range(n):
    (c, ti) = map(int, input().split())
    if ti <= t:
        cl.append(c)
print(min(cl) if cl != [] else 'TLE')
