n,m =map(int,input().split())
d = dict()
ans = 0
per1=0
per2 = 0
for j in range(n):
    per = input()
    d[per] = 0
for j in range(m):
    per = input()
    if per in d:
        ans += 1
if ans % 2 ==0:
    if m>=n:
        print('NO')
    else:
        print('YES')
else:
    n+=1
    if m>=n:
        print('NO')
    else:
        print('YES')
