N = int(input())
L = []
for i in range(N):
    A, B = list(map(int, input().split()))
    L.append((A, B))
L1 = sorted(L, key=lambda x: x[0])
L2 = sorted(L, key=lambda x: x[1])
if N % 2 == 1:
    n = N // 2
    print(L2[n][1] - L1[n][0] + 1)
else:
    n = N // 2
    m = (L1[n - 1][1] + L1[n][1]) / 2
    print(L2[n - 1][1] + L2[n][1] - L1[n - 1][0] - L1[n][0] + 1)
