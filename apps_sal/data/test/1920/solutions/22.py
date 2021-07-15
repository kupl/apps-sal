__author__ = 'Utena'
n=int(input())
m=[0]*366
f=[0]*366
for i in range(n):
    g,a,b=input().split()
    a,b=int(a),int(b)
    if g=='F':
        for i in range(a-1,b):
            f[i]+=1
    elif g=='M':
        for i in range(a-1,b):
            m[i]+=1
t=0
for i in range(366):
    temp=min(f[i],m[i])
    if temp>t:t=temp
print(t*2)
