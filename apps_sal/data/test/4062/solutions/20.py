l=[]
a,b,c,d=list(map(int,input().split()))
l.append(a*c)
l.append(a*d)
l.append(b*c)
l.append(b*d)
print((max(l)))

