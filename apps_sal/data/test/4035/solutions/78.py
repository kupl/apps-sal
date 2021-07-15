A,B = map(int,input().split())
left2 = B*10
right2 = (B+1)*10
if((A*100)/8 != int((A*100)/8)):
    left1 = int((A*100)/8)+1
else:
    left1 = (A*100)//8
if((A+1)*100/8 != int((A+1)*100/8)):
    right1 = (A+1)*100/8
else:
    right1 = ((A+1)*100//8) - 1
if(left1 >= left2 and right2 > left1):
    print(left1)
    return
if(left1 <= left2 and right1 > left2):
    print(left2)
    return
print(-1)
