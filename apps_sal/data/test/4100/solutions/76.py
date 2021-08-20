[N, K, Q] = [int(i) for i in input().split()]
P = [0] * N
for i in range(Q):
    a = int(input())
    P[a - 1] += 1
for i in range(N):
    if P[i] > Q - K:
        print('Yes')
    else:
        print('No')
