def solve():
    (N, K) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [a[0] - a[1] for a in zip(A, B)]
    D = list(zip(list(range(N)), C))
    D.sort(key=lambda tup: tup[1])
    cost = 0
    for i in range(K):
        cost += A[D[i][0]]
    j = K
    while j < N and D[j][1] <= 0:
        cost += A[D[j][0]]
        j += 1
    for i in range(j, N):
        cost += B[D[i][0]]
    print(cost)


solve()
