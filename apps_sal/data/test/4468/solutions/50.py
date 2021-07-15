n,t = map(int,input().split())
tlist = list(map(int,input().split()))
time = t
for i in range(0,n-1):
    if tlist[i+1]- tlist[i] <= t :
        time += tlist[i+1]- tlist[i]
    else:
        time += t
print(time)
