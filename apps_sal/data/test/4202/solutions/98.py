#ABC133 C

L,R = map(int,input().split())
A = []
if R - L > 2019:
    print(0)
elif 2 <= R - L and R - L <= 2019:
    for i in range(L,R):
        for j in range(i+1,R+1):
            A.append((i*j)%2019)
    print(min(A))
elif R - L == 1:
    print((R*L)%2019)
