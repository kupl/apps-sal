def fitVertical(A, B):
    if(B[0] <= A[0] and B[1] <= A[1]):
        return [A[0] - B[0], A[1] - B[1]]
    return [-1, -1]


def fitHorizontal(A, B):
    if(B[1] <= A[0] and B[0] <= A[1]):
        return [A[0] - B[1], A[1] - B[0]]
    return [-1, -1]


A = input().split()
B = input().split()
C = input().split()

A = [int(x) for x in A]
B = [int(x) for x in B]
C = [int(x) for x in C]

D = fitVertical(A, B)

if(D[0] != -1):

    if(fitVertical([D[0], A[1]], C)[0] != -1 or fitHorizontal([D[0], A[1]], C)[0] != -1):
        print("YES")
        return

    if(fitVertical([D[1], A[0]], C)[0] != -1 or fitHorizontal([D[1], A[0]], C)[0] != -1):
        print("YES")
        return

D = fitHorizontal(A, B)

if(D[0] != -1):

    if(fitVertical([D[0], A[1]], C)[0] != -1 or fitHorizontal([D[0], A[1]], C)[0] != -1):
        print("YES")
        return

    if(fitVertical([D[1], A[0]], C)[0] != -1 or fitHorizontal([D[1], A[0]], C)[0] != -1):
        print("YES")
        return

print("NO")
