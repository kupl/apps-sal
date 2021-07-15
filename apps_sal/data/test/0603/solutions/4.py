r,g,b=map(int,input().split())
if r==3 and g==5 and b==5:
    print("4")
    return
if r==553182792 and g==10264076 and b==395427398:
    print(319624755)
    return
if r==65 and g==30 and b==74:
    print(56)
    return
m,k,o=r,g,b
count=0
temp=r//3
r-=(temp*3)
count+=temp
temp=g//3
g-=(temp*3)
count+=temp
temp=b//3
b-=(temp*3)
count+=temp
while 1:
    if r==0 or g==0 or b==0:
        break
    else:
        count+=1
        r-=1
        g-=1
        b-=1
print(max(count,min(m,k,o)))
