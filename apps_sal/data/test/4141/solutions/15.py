import sys
N = int(input())
A = [int(n) for n in input().split()]

for i in range(N):
    if A[i] % 2 == 0:
        if A[i] % 3 ==0 or A[i] % 5 == 0:
            continue
        else:
            print('DENIED')
            return

print('APPROVED')
