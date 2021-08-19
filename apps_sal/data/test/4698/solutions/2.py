N = int(input())
T = list(map(int, input().split()))
M = int(input())
P = [list(map(int, input().split())) for i in range(M)]
tmp = 0
ans = 0
for i in range(M):
    tmp = 0
    for j in range(len(T)):
        if j == P[i][0] - 1:
            tmp += P[i][1]
        else:
            tmp += T[j]
    print(tmp)
