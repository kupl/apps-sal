lisa=[1,3,5,7,8,10,12]
lisb=[4,6,9,11]
lisc=[2]
x,y=map(int,input().split())
if (x in lisa)and(y in lisa):
    print("Yes")
elif (x in lisb)and(y in lisb):
    print("Yes")
elif (x in lisc)and(y in lisc):
    print("Yes")
else:
    print("No")
