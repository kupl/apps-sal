A = {}
for i in range(3) :
    a1,a2,a3 = map(int, input().split())
    A[a1] = (i,0)
    A[a2] = (i,1)
    A[a3] = (i,2)

N = int(input())
A2 = [[False,False,False] for i in range(3)]

for i in range(N):
    b = int(input())
    if(b not in A) :
        continue
    r,c = map(int,A[b])
    A2[r][c] = True

def isBingo(table) :
    for r in range(3) :
        if(table[r][0] and table[r][1] and table[r][2]) :
            return True
    for c in range(3) :
        if(table[0][c] and table[1][c] and table[2][c]) :
            return True
    if(table[0][0] and table[1][1] and table[2][2]) :
        return True
    if(table[0][2] and table[1][1] and table[2][0]) :
        return True
    return False

if(isBingo(A2)) :
    print("Yes")
else :
    print("No")
