n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
m = min(a)
t = a.count(m)
h = n - t
print((h//(k-1)+1-int(h%(k-1)==0)))

