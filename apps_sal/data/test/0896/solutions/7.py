I=input
P=print
R=range
I()
a=[int(i)for i in I().split()]
b=[int(i)for i in I().split()]
n=len(a)
m=len(b)
x=b[-1]
for i in R(n-1):x^=a[i]
y=a[-1]
for i in R(m-1):y^=b[i]
if x!=y:P("NO");return
P("YES")
for i in R(n-1):P("0 "*(m-1)+str(a[i]))
for i in R(m-1):P(b[i],end=" ")
P(x)
