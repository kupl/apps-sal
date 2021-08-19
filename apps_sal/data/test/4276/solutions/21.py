(N, T) = map(int, input().split())
ls = []
for i in range(N):
    (c, t) = map(int, input().split())
    if t <= T:
        ls.append(c)
print(min(ls) if ls else 'TLE')
