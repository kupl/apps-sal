a,b=[int(c) for c in input().split(' ')]
c,d=[int(c) for c in input().split(' ')]


i=0
max=pow(10,5)
while b!=d and i<max:
    while d<b:
        d+=c
    while b<d:
        b+=a
    i+=1

if b!=d:
    print(-1)
else:
    print(d)
