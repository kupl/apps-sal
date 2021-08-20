(n, m) = map(int, input().strip().split())
on = set()
for _ in range(n):
    on |= set(list(map(int, input().strip().split()))[1:])
if len(on) == m:
    print('YES')
else:
    print('NO')
