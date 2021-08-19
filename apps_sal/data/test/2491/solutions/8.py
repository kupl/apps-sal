(N, M) = map(int, input().split())
adjacent = []
score = ['None' for i in range(N)]
score[0] = 0
for i in range(M):
    (a, b, c) = map(int, input().split())
    adjacent.append([a - 1, b - 1, c])
for i in range(N):
    for j in adjacent:
        if score[j[1]] == 'None' and score[j[0]] != 'None':
            score[j[1]] = score[j[0]] + j[2]
        if score[j[1]] != 'None' and score[j[0]] != 'None':
            if score[j[1]] < score[j[0]] + j[2]:
                score[j[1]] = score[j[0]] + j[2]
    if i == N - 2:
        t = score[N - 1]
    if i == N - 1:
        if t != score[N - 1]:
            score[N - 1] = 1000000000000000.0
if score[N - 1] < 1000000000000000.0:
    print(t)
else:
    print('inf')
