N = int(input())
P = [[0, 0, 0]]
for i in range(N):
    (t, x, y) = list(map(int, input().split()))
    P.append([t, x, y])
judge = True
for i in range(1, N + 1):
    dt = P[i][0] - P[i - 1][0]
    dist = abs(P[i][1] - P[i - 1][1]) + abs(P[i][2] - P[i - 1][2])
    if dt % 2 == 0 and dist % 2 == 0 and (dist <= dt) or (dt % 2 == 1 and dist % 2 == 1 and (dist <= dt)):
        judge = True
    else:
        judge = False
if judge:
    print('Yes')
else:
    print('No')
