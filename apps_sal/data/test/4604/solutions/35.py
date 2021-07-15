N = int(input())
A = list(map(int, input().split()))
mod = pow(10,9)+7
A.sort()

if N%2 == 0:
    for i in range(N//2):
        if A[2*i] != A[2*i+1] or A[2*i] != 2*i+1:
            print((0))
            return
    ans = pow(2,N//2)
    print((ans%mod))
else:
    if A[0] != 0:
        print((0))
        return
    for i in range(N//2):
        if A[2*i+1] != A[2*(i+1)] or A[2*i+1] != 2*(i+1):
            print((0))
            return
    ans = pow(2,N//2)
    print((ans%mod))

