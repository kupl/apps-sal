n=int(input())
l1=list(map(int,input().split()))
x=[4,8,15,16,23,42]
count=[0]*6
for item in l1:
    if item==4:
        count[0]+=1
    elif item==8:
        if count[0]>count[1]:
            count[1]+=1
    elif item==15:
        if count[1]>count[2]:
            count[2]+=1
    elif item==16:
        if count[2]>count[3]:
            count[3]+=1
    elif item==23:
        if count[3]>count[4]:
            count[4]+=1
    elif item==42:
        if count[4]>count[5]:
            count[5]+=1
print(n-6*count[5])

