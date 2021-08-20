(N, K, Q) = list(map(int, input().split()))
M = []
for i in range(N):
    M.append(K - Q)
for j in range(Q):
    a = int(input())
    M[a - 1] += 1
for k in range(N):
    if M[k] <= 0:
        print('No')
    else:
        print('Yes')
