N=int(input())
*A,=sorted(map(int,input().split()))

f=lambda:2**(N//2)%(10**9+7)
a=True
if N%2==0:
    for i in range(1,N,2):
        if A[i-1]!=i or A[i]!=i:
            # print(i,A[i-1],A[i])
            a=False
            break
else:
    if A[0]!=0:
            a=False
    else:
        for i in range(2,N,2):
            if A[i-1]!=i or A[i]!=i:
                # print(i,A[i-1],A[i])
                a=False
                break
print(f() if a else 0)
