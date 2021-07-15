k, w, n = [int(i) for i in input().split()]
t = k*n*(n+1)//2-w
if t>0:
    print(t)
else:
    print(0)

