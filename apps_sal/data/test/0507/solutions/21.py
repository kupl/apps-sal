import sys
read=lambda:sys.stdin.readline().rstrip()
readi=lambda:int(sys.stdin.readline())
writeln=lambda x:sys.stdout.write(str(x)+"\n")
write=lambda x:sys.stdout.write(x)
N = readi()
A = list(map(int, read().split()))
B = list(map(int, read().split()))
ncntA = [0]*(N+1)
ncntB = [0]*(N+1)
diff = []
for i in range(N):
    if A[i] != B[i]:
        diff.append(i)
    ncntA[A[i]] += 1
    ncntB[B[i]] += 1

if len(diff) == 2:
    P = list(A)
    P[diff[0]] = B[diff[0]]
    
    ncntP = [0]*(N+1)
    for i in range(N):
        ncntP[P[i]] += 1

    flag = False
    for i in range(1, N+1):
        if ncntP[i] == 0:
            flag = True
            break
    if flag:
        P = list(A)
        P[diff[1]] = B[diff[1]]

    writeln(' '.join(str(c) for c in P))
else:
    k = -1
    for i in range(1, N+1):
        if ncntA[i] == 0 and ncntB[i] == 0:
            k = i
            break
    P = list(A)
    P[diff[0]] = k
    writeln(' '.join(str(c) for c in P))
