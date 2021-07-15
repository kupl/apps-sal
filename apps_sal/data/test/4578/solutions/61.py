a,b=input().split()
a=int(a)
b=int(b)
c=[int(input()) for i in range(a)]
c.sort()
print(a+int((b-sum(c))/c[0]))
