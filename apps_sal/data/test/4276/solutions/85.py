N, T = list(map(int, input().split()))

m = 1001

for i in range(N):

    c, t = list(map(int, input().split()))

    if t <= T:
        m = min(m, c)

print(("TLE" if m == 1001 else m))
