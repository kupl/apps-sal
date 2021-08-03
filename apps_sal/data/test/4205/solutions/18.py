N = int(input())
p = list(map(int, input().split()))
q = list(range(1, N + 1))

ans = 0
for i in range(N):
    if p[i] != q[i]:
        ans += 1

if ans <= 2:
    print('YES')
else:
    print('NO')
