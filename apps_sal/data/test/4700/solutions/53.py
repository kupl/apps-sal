n,m = map(int,input().split())
h = list(map(int,input().split()))
flg = [1]*n
for _ in range(m):
    a,b = map(int,input().split())
    if h[a-1] > h[b-1]:
        flg[b-1] = 0
    elif h[a-1] == h[b-1]:
        flg[a-1],flg[b-1] = 0,0
    else:
        flg[a-1] = 0
print(flg.count(1))
