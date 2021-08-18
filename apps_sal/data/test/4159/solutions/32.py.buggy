A, B, K = map(int, input().split())
if(A - K >= 0):
    A -= K
    print(A, B)
    return
if(A - K < 0):
    K -= A
    A = 0
    B -= K
    if(B < 0):
        print(0, 0)
        return
    print(A, B)
