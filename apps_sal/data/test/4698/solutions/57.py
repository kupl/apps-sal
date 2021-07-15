N = int(input())
T = list(map(int, input().split()))
M = int(input())
P, X = [0] * M, [0] * M
for i in range(M):
    P[i], X[i] = map(int, input().split())

for i in range(M):
    t_sum = X[i]
    for j in range(N):
        if j == P[i] - 1:
            continue
        t_sum += T[j]
    print(t_sum)
