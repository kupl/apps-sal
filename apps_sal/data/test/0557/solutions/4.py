(n, m) = list(map(int, input().split()))
pos = 0
for _ in range(n):
    (a, b) = list(map(int, input().split()))
    if a > pos:
        break
    pos = max([pos, b])
if pos >= m:
    print('YES')
else:
    print('NO')
