N, K, Q = list(map(int, input().split()))
A = [int(input()) for _ in range(Q)]

li = [0 for _ in range(N)]
for i in range(Q):
    li[A[i]-1] += 1

for i in range(N):
    if Q - K + 1 <= li[i]:
        print('Yes')
    else:
        print('No')

