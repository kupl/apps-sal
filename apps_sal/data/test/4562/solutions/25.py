import sys
N=int(input())
if N==1:
    print("1")
elif N==2:
    print("1")
else:
    for i in range(N):
        if i**2>N:
            print((i-1)**2)
            return
        else:
            pass
