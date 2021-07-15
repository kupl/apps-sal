N,D = map(int,input().split())
if(N % (D*2+1) != 0):
    print((N // (D*2+1)) + 1)
else:
    print(N // (D*2+1))
