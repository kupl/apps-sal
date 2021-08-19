(N, K, Q) = map(int, input().split())
scores = [K - Q] * (N + 1)
for i in range(Q):
    a = int(input())
    scores[a] += 1
for i in range(1, N + 1):
    if scores[i] <= 0:
        print('No')
    else:
        print('Yes')
