n, m = map(int, input().split())
rm = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a > rm:
        print('NO')
        return
    rm = max(rm, b)
if rm >= m:
    print('YES')
else:
    print('NO')
