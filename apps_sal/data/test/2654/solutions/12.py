n = int(input())
a = []
b = []
for i in range(n):
    s,t = map(int,input().split())
    a.append(s)
    b.append(t)
a.sort()
b.sort()
if n%2 == 0:
    am = (a[n//2-1]+a[n//2])/2
    bm = (b[n//2-1]+b[n//2])/2
    print(int((bm-am)*2+1))
else:
    am = a[(n-1)//2]
    bm = b[(n-1)//2]
    print(bm-am+1)
