N, T = map(int, input().split())
ans = 10000

for _ in range(N):
    c,t = map(int, input().split())
    if t <= T:
        ans = min(ans,c)
if ans == 10000:
    print ('TLE')
else:
    print (ans)
