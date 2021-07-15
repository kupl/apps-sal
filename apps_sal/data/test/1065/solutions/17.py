Q = [int(x) for x in input().split(' ')]
n = Q[0]
k = Q[1]
M = Q[2]
D = Q[3]

mm = 0

for i in range(D):
    m = n // (i * k + 1)
    if m > M:
        m = M
    mm = max(m * (i + 1), mm)

print(mm)

