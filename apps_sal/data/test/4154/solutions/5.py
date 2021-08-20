(N, M) = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(M)]
max_l = 0
min_r = 10 ** 9
for i in range(M):
    if max_l <= LR[i][0]:
        max_l = LR[i][0]
    if min_r >= LR[i][1]:
        min_r = LR[i][1]
print(max(0, min_r - max_l + 1))
