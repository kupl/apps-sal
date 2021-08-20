(N, K, Q) = map(int, input().split())
getp = [0 for _ in range(N)]
for _ in range(Q):
    A = int(input())
    getp[A - 1] += 1
for i in range(N):
    if K - Q + getp[i] > 0:
        print('Yes')
    else:
        print('No')
