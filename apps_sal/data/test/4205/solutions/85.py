N = int(input())
P = list(map(int, input().split()))
ido = []
for i in range(N):
    if P[i] != i + 1:
        ido.append(P[i])
if len(ido) == 2 or len(ido) == 0:
    print('YES')
else:
    print('NO')
