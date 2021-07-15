N, K = map(int,input().split())
ls = [0]+[0]*10**5
for i in range(N):
    a,b = map(int,input().split())
    ls[a] += b
ii = 0
for i in range(1,10**5+1):
    ii += ls[i]
    if ii >= K:
        ans = i
        break
    else:
        continue
print(ans)
