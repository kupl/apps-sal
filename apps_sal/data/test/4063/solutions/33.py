N=int(input())
d=list(map(int,input().split()))
d.sort()
l=d[:N//2]
r=d[N//2:]

print(r[0]-l[-1])
