N, K, Q = list(map(int, input().split()))

L = [K] * N

for i in range(Q):
    A = int(input())
    L[A - 1] += 1

for i in L:
    if i - Q > 0:
        print('Yes')
    else:
        print('No')
