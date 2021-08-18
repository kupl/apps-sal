[N, M, X] = list(map(int, list(input().split(' '))))
A = []
C = []
for i in range(N):
    c, *a = list(map(int, input().split(' ')))
    C.append(c)
    A.append(a)

INF = 10**10
min_cost = INF

for b in range(2**N):
    cost = 0
    algo_level = [0] * M
    for i in range(N):
        if(b >> i & 1):
            cost += C[i]
            for a in range(M):
                algo_level[a] += A[i][a]
    if(min(algo_level) >= X):
        min_cost = min(cost, min_cost)

if(min_cost < INF):
    print(min_cost)
else:
    print('-1')
