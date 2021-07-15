N,A,B=map(int,input().split())
if N%(A+B)>A:
    print(int(N/(A+B))*A+A)
else:
    print(int(N/(A+B))*A+N%(A+B))
