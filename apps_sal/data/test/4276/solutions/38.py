N, T = list(map(int, input().split()))
c = [0] * N
t = [0] * N
for i in range(N):
    c[i], t[i] = list(map(int, input().split()))

z = list(zip(c, t))
z = sorted(z)
c, t = list(zip(*z))

for i in range(N):
    if t[i] <= T:
        print((c[i]))
        return
print('TLE')
