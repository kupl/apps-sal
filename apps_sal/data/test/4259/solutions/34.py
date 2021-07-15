k = int(input())
a, b = map(int,input().split())

ans = 0
for i in range(a,b+1):
    if i % k == 0:
        ans += 1

if ans == 0 :
    print('NG')
    
else :
    print('OK')
