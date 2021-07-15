a,b,c=[int(i) for i in input().split()]
d=0
while d<1000:
    d+=1
    if str(a*(10**d)//b)[-1]==str(c):
        print(d)
        return
print(-1)
    

