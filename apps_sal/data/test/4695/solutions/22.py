a=[1,3,5,7,8,10,12]
b=[4,6,9,11]
c=list(map(int,input().split(" ")))
print("Yes") if (c[0] in a and c[1] in a) or (c[0] in b and c[1] in b) else print("No")
