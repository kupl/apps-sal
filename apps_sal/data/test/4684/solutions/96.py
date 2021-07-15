r, g, b = map(int,input().split())
ans = 100*r + 10 *g + b
if ans % 4 == 0:
    print('YES')
else :
    print('NO')
