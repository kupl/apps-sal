#ABC164
A,B,C,D=map(int,input().split())
while A > 0:
    C += -1*B
    if C <= 0:
        print('Yes')
        break
    A += -1*D
    if A <= 0:
        print('No')
        break
