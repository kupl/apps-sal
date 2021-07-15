A,B = map(int,input().split())
A2 = bin(A)[2:]
B2 = bin(B)[2:]
N = len(B2)
A2 = "0"*(N-len(A2))+A2
C = [0 for _ in range(N)]
T = B-A
for k in range(N):
    ind = A%(2**(k+1))
    if k==0:
        t = T%(2**(k+2))
        s = "01010101"
        c1 = 0
        for i in range(ind,ind+t+1):
            if s[i]=="1":
                c1 += 1
    else:
        t = T%(2**(k+1))
        if ind<2**k:
            if ind+t<2**k:
                c1 = 0
            elif ind+t<2**(k+1):
                c1 = ind+t-(2**k-1)
            else:
                c1 = 2**k
        else:
            if ind+t<2**(k+1):
                c1 = t+1
            elif ind+t<3*(2**k):
                c1 = 2**(k+1)-ind
            else:
                c1 = t-2**k+1
    C[N-1-k] = c1%2
a = 0
for i in range(N):
    a = 2*a+C[i]
print(a)
