N = int(input())
A = [int(i) for i in input().split()]

if min(A) >= 0:
    print((N-1))
    for i in range(N-1):
        print((i+1, i+2))
elif max(A) < 0:
    print((N-1))
    for i in range(N-1):
        print((N-i, N-1-i))
else:
    if max(A) >= abs(min(A)):
        print((2*N-1))
        for i in range(N):
            print((A.index(max(A))+1, i+1))
        for i in range(N-1):
            print((i+1, i+2))
    else:
        print((2*N-1))
        for i in range(N):
            print((A.index(min(A))+1, i+1))
        for i in range(N-1):
            print((N-i, N-1-i))

