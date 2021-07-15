a = input().split(' ')
b = input().split(' ')
n=int(a[1])
x=int(a[2])
y=int(a[3])
xcan=False
ycan=False
xycan=False
xymoar=False
cool=0
cool2=0
s=set()
for element in b:
    s.add(int(element))
for c in s:
    if c+x in s:
        xcan=True
    if c+y in s:
        ycan=True
    if c+x+y in s:
        xycan = True
        cool=c
    if c+y-x in s:
        if c+y>n:
            if c-x<0:
                pass
            else:
                cool2 = c-x
                xymoar=True
        else:
            xymoar = True
            cool2 = c+y
    if xcan:
        if ycan:
            break
if xcan==True:
    if ycan==True:
        result=0
        marks=[]
    else:
        result = 1
        marks=[y]
else:
    if ycan == True:
        result = 1
        marks=[x]
    else:
        if xycan == True:
            result=1
            marks=[cool+x]
        elif xymoar == True:
            result=1
            marks=[cool2]
        else:
            result=2
            marks=[x,y]
print(result)
for i in range(len(marks)):
    print(marks[i], end=' ')
