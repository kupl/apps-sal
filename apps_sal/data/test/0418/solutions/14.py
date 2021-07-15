won = False
for i in range(int(input())):
    n, f, s = input().split()
    f = int(f)
    s = int(s)
    if s > f and f >= 2400:
        won = True
if won:
    print('YES')
else:
    print('NO')
