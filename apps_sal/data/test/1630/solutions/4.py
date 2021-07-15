from sys import stdin

n = int(stdin.readline().strip())
T,A = [],[]
N,M = {},{}
for _ in range(n):
    t,h = stdin.readline().split()
    n1,n2 = t[:3],t[:2]+h[0]
    N[n1] = N.get(n1,0)+1
    T.append((n1,n2))
    A.append(n1)

def solve():
    for i in range(n):
        n1,n2 = T[i]
        if n1 not in M and N[n1]==1:
            M[n1] = i
            continue
        while n2 in M:
            j = M[n2]
            if n2==T[j][1]:
                return False
            M[n2],A[i]=i,n2
            i,n2 = j,T[j][1]
        else:
            M[n2],A[i] = i,n2
    return True

if solve():
    print("YES")
    print('\n'.join(A))
else:
    print("NO")

