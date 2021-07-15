def f(s):
    A = [int(i) for i in s.split()]
    first = 0
    for i in range(0,len(A)-1,2):
        first += abs(A[i+1]-A[i])
    second = 0
    for i in range(0,len(A)-1,2):
        second += A[i]-A[i+1]
    second = abs(second)
    return first -second


'''
For a given n, if k=n+2, do [n-1, n-2, ..., 1, n]

'''
n, k = [int(i) for i in input().split()]
k = 2*k
if k == 0:
    print(*[i for i in range(1,2*n+1)])
elif k==2*n:
    print(2*n,end=' ')
    for i in range(2*n-2,0,-1):
        print(i,end=' ')

    print(1)
else:
    for i in range(k+1,0,-1):
        print(i,end=' ')
    for i in range(k+2,2*n+1):
        print(i,end=' ')
    print()

