l=[int(i) for i in input().split(" ")]
k=l[0]
a=l[1]
b=l[2]
v=l[3]
box=0
divs=0
while a>0:
    box+=1
    sections=1
    a-=v
    while a>0 and sections<k and divs<b:
        divs+=1
        sections+=1
        a-=v
print(box)
