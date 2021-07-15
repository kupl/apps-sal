L = int(input())
A = input()
N = len(A)

if N%L != 0 or A == '9'*N:
    K = N//L + 1
    for _ in range(K):
        print(1, end='')
        for _ in range(L-1):
            print(0, end='')
    print()
else:
    for k in range(N//L):
        lg = 0
        for l in range(L):
            a0 = int(A[l])
            a = int(A[k*L+l])
            if a > a0:
                lg = 1
                break
            if a < a0:
                lg = -1
                break
        if lg == -1 or lg == 1:
            break
    if lg == -1:
        for _ in range(N//L):
            print(A[:L], end='')
        print()
    elif lg == 1 or lg == 0:
        B = list(A[:L])
        for l in range(L):
            b = int(B[L-1-l])+1
            if b == 10:
                B[L-1-l] = '0'
            else:
                B[L-1-l] = str(b)
                break
        for _ in range(N//L):
            print(''.join(B), end='')
        print()

