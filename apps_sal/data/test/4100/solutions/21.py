(N, K, Q) = map(int, input().split())
dct = {}
for _ in range(Q):
    A = int(input())
    if A in dct:
        dct[A] += 1
    else:
        dct[A] = 1
x = Q - K
if x < 0:
    for _ in range(N):
        print('Yes')
else:
    for i in range(1, N + 1):
        if i in dct and dct[i] >= x + 1:
            print('Yes')
        else:
            print('No')
