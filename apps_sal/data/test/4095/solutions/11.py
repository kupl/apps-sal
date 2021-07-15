L1=list(map(int, input().split()))
numList=list(map(int, input().split()))
length=L1[0]
targetnumber=L1[1]
pos=numList.index(targetnumber)
pos_r=pos+1
rem=0
right={0:1}
left={0:1}
while pos_r<=length-1:
    if numList[pos_r]>targetnumber:
        rem+=1
    else:
        rem-=1
    if rem not in right:
        right[rem]=1
    else:
        right[rem]+=1
    pos_r+=1
pos_l=pos-1
rem=0
while pos_l>=0:
    if numList[pos_l]>targetnumber:
        rem+=1
    else:
        rem-=1
    if rem not in left:
        left[rem]=1
    else:
        left[rem]+=1
    pos_l-=1
sum=0
for number_l in left:
    if number_l*(-1) in right:
        sum += (left[number_l] * right[(-1) * number_l])
    if 1-number_l in right:
        sum += (left[number_l] * right[1-number_l])
print(sum)
