y,b=map(int,input().split())
A=list(map(int,input().split()))
yn=2*A[0]+A[1]
bn=A[1]+3*A[2]
ym=max(0,yn-y)
bm=max(0,bn-b)
print(ym+bm)
