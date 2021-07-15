n = int(input())
s= list(map(int,input().split()))
count = [0]*6
for temp in s:
    if temp==4:
        count[0]+=1
    elif temp==8 and count[0]>count[1]:
        count[1]+=1
    elif temp==15 and count[1]>count[2]:
        count[2]+=1
    elif temp==16 and count[2]>count[3]:
        count[3]+=1
    elif temp==23 and count[3]>count[4]:
        count[4]+=1
    elif temp==42 and count[4]>count[5]:
        count[5]+=1
    else:
        pass
#print(count)
out = n - 6*min(count)
print(out)
