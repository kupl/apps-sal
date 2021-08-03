N, M = map(int, input().split())
x = [0] * N
y = [0] * N
P = []
s = []

for i in range(M):
    p, S = map(str, input().split())
    P.append(int(p))
    s.append(S)
for j in range(M - 1, -1, -1):
    if s[j] == 'AC':
        if x[P[j] - 1] == 0:
            x[P[j] - 1] = 1
        else:
            y[P[j] - 1] = 0
    elif s[j] == 'WA':
        if x[P[j] - 1] == 1:
            y[P[j] - 1] += 1
print(x.count(1), sum(y))
