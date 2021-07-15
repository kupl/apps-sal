A,B,C = (list(input()) for T in range(0,3))
Next = A.pop(0)
while True:
    if Next=='a':
        if not len(A):
            print('A')
            break
        Next = A.pop(0)
    elif Next=='b':
        if not len(B):
            print('B')
            break
        Next = B.pop(0)
    else:
        if not len(C):
            print('C')
            break
        Next = C.pop(0)
