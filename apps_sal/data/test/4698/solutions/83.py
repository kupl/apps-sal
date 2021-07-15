N = int(input())
T = list(map(int, input().split()))
M = int(input())
L = []
for _ in range(M):
    p, x = list(map(int, input().split()))
    L.append([p, x])

for i in range(M):
    sum_num = 0
    for j in range(N):
        if L[i][0] - 1 == j:
            sum_num += L[i][1]
        else:
            sum_num += T[j]
    print(sum_num)

