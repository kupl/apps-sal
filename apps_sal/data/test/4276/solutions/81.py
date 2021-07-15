n,t = list(map(int,input().split()))
ans = 9999
for i in range(n):
    ci,ti = list(map(int,input().split()))
    if ti<=t:
        ans = min(ans,ci)
if ans == 9999:
    print('TLE')
else:
    print(ans)

