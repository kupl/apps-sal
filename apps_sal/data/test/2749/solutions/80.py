H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))
D = {}
for i in range(N):
    D[i + 1] = A[i]
C = []
for k, v in D.items():
    [C.append(k) for _ in range(v)]
h = 0
while True:
    h += 1
    for i in range(W):
        print(C[i], end=' ')
    print('')
    [C.pop(0) for _ in range(W)]
    if h == H:
        break
    h += 1
    for i in reversed(range(W)):
        print(C[i], end=' ')
    print('')
    [C.pop(0) for _ in range(W)]
    if h == H:
        break
