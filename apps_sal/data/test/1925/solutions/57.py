A,B,N = map(int,input().split())
if B-1 <= N:
    print((A*(B-1))//B)
else:
    print((A*N)//B)
