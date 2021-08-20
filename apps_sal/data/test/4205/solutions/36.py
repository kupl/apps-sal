N = int(input())
p = list(map(int, input().split()))
ans = 0
for i in range(N):
    if p[i] != i + 1:
        ans += 1
if ans <= 2:
    print('YES')
else:
    print('NO')
