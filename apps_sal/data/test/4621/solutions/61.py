(x, y) = map(int, input().split())
L = []
for _ in range(x):
    N = list(input())
    L.append(N)
    L.append(N)
for l in L:
    print(''.join(l))
