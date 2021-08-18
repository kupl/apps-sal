N = int(input())
p = list(map(int, input().split()))


q = list(range(1, N + 1))

k = 0
for i in range(N):
    if p[i] != q[i]:
        k += 1

if k <= 2:
    print('YES')
else:
    print('NO')
