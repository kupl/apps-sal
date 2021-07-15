
r,g,b = map(int,input().split())
a = r *100+g*10+b
if a % 4 == 0:
    print('YES')
else:
    print('NO')
