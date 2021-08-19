(n, t) = (int(input()), list(map(int, input().split())))
(p, t) = ([0] * 3, t + [0] * (3 - n % 3))
for i in range(0, n, 3):
    for j in range(3):
        p[j] += t[i + j]
print(['chest', 'biceps', 'back'][p.index(max(p))])
