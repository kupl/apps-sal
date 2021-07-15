def ok( AA , resB ):
    realB = []
    for i in range(0,m):
        realBrow = []
        for j in range(0,n):
            res = 0
            for k in range(0,m):
                res += AA[k][j]
            for k in range(0,n):
                res += AA[i][k]
            if res > 0:
                res = 1
            realBrow.append( res )
        realB.append( realBrow )

    for i in range(0,m):
        for j in range(0,n):
            if realB[i][j] != resB[i][j]:
                return False
    return True

[m,n] = input().split(" ")
m = int(m)
n = int(n)
#print("m:%d n:%d" % ( m , n ) )

B = []
A = []
for i in range(0,m):
    brow = input().split(" ")
    arow = []
    for j in range(0,n):
        brow[j] = int(brow[j])
        arow.append(1)
    B.append( brow )
    A.append( arow )

#print(B)
for i in range(0,m):
    for j in range(0,n):
        if B[i][j] == 0:
            for k in range(0,m):
                A[k][j] = 0
            for k in range(0,n):
                A[i][k] = 0

if ok(A,B):
    print("YES")
    for i in range(0,m):
        for j in range(0,n):
            A[i][j] = str(A[i][j])
        print(" ".join(A[i]))
else:
    print("NO")




