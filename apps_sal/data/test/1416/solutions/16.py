n, w = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
c = (w/3)/n
a.sort()
if a[0] > c and a[n] > 2*c:
    print(w)
else:
     print(min(a[n]/2, a[0])*3*n)
    

