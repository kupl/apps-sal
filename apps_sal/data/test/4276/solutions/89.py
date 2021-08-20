(N, T) = map(int, input().split())
C = 1001
for i in range(N):
    (c, t) = map(int, input().split())
    if t <= T and c < C:
        C = c
if C == 1001:
    print('TLE')
else:
    print(C)
