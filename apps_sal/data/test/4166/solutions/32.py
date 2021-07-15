N,M = map(int,input().split())
S = []
C = []
a = 10**(N-1)
b = 10**N
if(N == 1):
    a = 0
for i in range(M):
    s,c = map(int,input().split())
    S.append(s)
    C.append(c)
for i in range(a,b):
    count = 0
    num = str(i)
    for j in range(M):
        if(num[S[j]-1] == str(C[j])):
            count += 1
    if(count == M):
        print(i)
        return
print(-1)
