n,k,b = map(int,input().split())
m = int(input())+1
b += 1
a = list(map(int,input().split()))
l,r = 0,m
while r-l > 1:
    d = (l+r)//2
    c = sorted(a[:d])
    if sum([(p-q)//b for q,p in zip([0]+c,c+[n+1])]) >= k:
        l = d
    else:
        r = d
print(r%m-(r==m))
