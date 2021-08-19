(N, T) = map(int, input().split())
k = 1000
l = 1
for i in range(N):
    (c, t) = map(int, input().split())
    if t <= T:
        l = 0
        if c < k:
            k = c
if l == 1:
    print('TLE')
else:
    print(k)
