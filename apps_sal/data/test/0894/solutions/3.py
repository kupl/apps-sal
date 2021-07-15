x,y=map(int,input().split())



#y=-x+c
if((x>0 and y>0)):
    c=y+x
    print("0 "+str(c),end=" ")
    print(str(c)+" 0")
elif(x<0 and y<0):
    c=y+x
    print(str(c)+" 0",end=" ")
    print("0 "+str(c))
    
elif(y>x):
    c=y-x
    print(str(-1*c)+" 0",end=" ")
    print("0 "+str(c))
else:
    c=y-x
    print("0 "+str(c),end=" ")
    print(str(-1*c)+" 0")
    

