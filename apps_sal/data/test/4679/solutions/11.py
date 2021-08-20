A = input()
B = input()
C = input()
n = A[0]
A = A[1:]
while True:
    if n == 'a':
        if len(A) == 0:
            print('A')
            break
        n = A[0]
        A = A[1:]
    elif n == 'b':
        if len(B) == 0:
            print('B')
            break
        n = B[0]
        B = B[1:]
    else:
        if len(C) == 0:
            print('C')
            break
        n = C[0]
        C = C[1:]
