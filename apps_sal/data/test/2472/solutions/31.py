import operator

N = int(input())
work = sorted([tuple(map(int, input().split())) for _ in range(N)], key=operator.itemgetter(1), reverse=True)

t = work[0][1]

for i in range(N):
    if t > work[i][1]:
        t = work[i][1]
    t -= work[i][0]

print(['No', 'Yes'][t >= 0])
