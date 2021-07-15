a,b,c,d=map(int,input().split())

e=c-(d-b)
f=d+(c-a)
g=e-(c-a)
h=f-(d-b)

print("{} {} {} {}".format(e,f,g,h))
