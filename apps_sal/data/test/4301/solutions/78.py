#ABC134 C (再考察)

N = int(input())
A = []
for i in range(N):
    a = int(input())
    A.append(a)
    
AA = sorted(A,reverse = True)
for i in range(N):
    if A[i] != AA[0]:
        print(AA[0])
    else:
        print(AA[1])
