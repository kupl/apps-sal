n,w=list(map(int,input().split()))
ls = list(map(int,input().split()))
ls.sort()
mi = min(ls[0],ls[n]/2)
print(min(w,(3*mi*n)))

