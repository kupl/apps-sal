(N, M) = [int(x) for x in input().split(' ')]
next_to_1 = []
next_to_last = []
for i in range(M):
    tmp = input().split(' ')
    if int(tmp[0]) == 1:
        next_to_1.append(int(tmp[1]))
    if int(tmp[1]) == N:
        next_to_last.append(int(tmp[0]))
if len(list(set(next_to_1) & set(next_to_last))) > 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
