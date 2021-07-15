A=[list(map(int,input().split())) for i  in range(3)]
if A[0][0]+A[1][1]==A[0][1]+A[1][0] and A[1][1]+A[2][2]==A[1][2]+A[2][1] and A[0][0]+A[2][2]==A[0][2]+A[2][0] :
    print("Yes")
else:
    print("No")
