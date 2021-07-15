a,b = map(int,input().split())
l=[]
l.append(a+b)
l.append(a-b)
l.append(a*b)
print(max(l))
