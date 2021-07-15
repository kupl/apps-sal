l=input()
m=l.split(' ')
(a,b,c,d)=(int(m[0]),int(m[1]),int(m[2]),int(m[3]))
ans=1/(1+(b*c)/(a*d)-(c/d))
print(ans)

