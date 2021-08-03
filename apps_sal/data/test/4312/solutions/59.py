A, B, C, D = map(int, input().split())
while(A > 0 and C > 0):
    C -= B
    if(C > 0):
        A -= D
if(C <= 0):
    print("Yes")
    return
if(A <= 0):
    print("No")
