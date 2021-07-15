"""
各山のgrundy数がわかればよい

基本的にループする
"""

N = int(input())

ans = 0

for i in range(N):

    A,K = list(map(int,input().split()))

    

    while True:

        if A % K == 0:
            ans ^= A // K
            break

        elif A == K-1:
            ans ^= 0
            break

        else:

            if A // K != (A - A//K -1) // K:
                A = A - A // K - 1
            else:
                A -= (A - (A // K) * K) // (A // K+1) * (A//K+1)

    

if ans == 0:
    print ("Aoki")
else:
    print ("Takahashi")

