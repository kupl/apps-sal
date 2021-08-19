n = int(input())
p = list(map(int, input().split()))
new_p = sorted(p)
cnt = 0
for i in range(n):
    if p[i] != new_p[i]:
        cnt += 1
if cnt > 2:
    print('NO')
else:
    print('YES')
