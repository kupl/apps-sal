(N, M) = map(int, input().split())
prob = [[0, 0] for i in range(N)]
for i in range(M):
    (p, S) = input().split()
    x = int(p) - 1
    if prob[x][0] == 0 and S == 'WA':
        prob[x][1] += 1
    elif prob[x][0] == 0 and S == 'AC':
        prob[x][0] = 1
(ACs, WAs) = (0, 0)
for i in range(N):
    if prob[i][0] == 1:
        ACs += 1
        WAs += prob[i][1]
print(ACs, ' ', WAs)
