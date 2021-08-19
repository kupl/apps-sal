(N, T) = map(int, input().split())
lst = []
for i in range(N):
    (c, t) = map(int, input().split())
    if t <= T:
        lst.append(c)
if not lst:
    print('TLE')
else:
    print(min(lst))
