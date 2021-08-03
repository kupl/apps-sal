n = int(input())
A = list(map(int, input().split()))

if A[0] % 2 == 0 or A[-1] % 2 == 0 or len(A) % 2 == 0:
    print('No')
else:
    print('Yes')
