a=int(input())
b,c=input().split()
b=int(b)
c=int(c)
e=0
d=[int(input()) for i in range(a)]
for i in range(a):
  e=e+int((b-1)/d[i])+1
print(e+c)
