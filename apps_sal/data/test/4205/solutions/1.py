N = int(input())
P = list(map(int, input().split()))
A = list(range(1, N + 1))
count = 0
for i in range(N):
    if P[i] != A[i]:
        count += 1
if count <= 2:
    print('YES')
else:
    print('NO')
