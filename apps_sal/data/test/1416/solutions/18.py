n,w=map(int,input().split())
a=[int(x) for x in input().split()]
a.sort()
print(min(a[0],a[n]/2,w/(3*n))*3*n)
