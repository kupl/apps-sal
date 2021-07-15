x,y=list(map(int,input().split()))
A={1,3,5,7,8,10,13}
B={4,6,9,11}
C={2}

if (x in A and y in A) or (x in B and y in B) or (x in C and y in C):
    print("Yes")
else:
    print("No")

