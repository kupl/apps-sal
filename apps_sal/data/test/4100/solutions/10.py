(N, K, Q) = map(int, input().split())
pointList = [0] * N
for i in range(Q):
    A = int(input())
    pointList[A - 1] += 1
for i in range(N):
    if Q - pointList[i] < K:
        print('Yes')
    else:
        print('No')
