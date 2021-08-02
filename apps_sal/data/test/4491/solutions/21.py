import itertools
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

maxi = 0

for i in range(N):
    if sum(A[0:i + 1]) + sum(B[i:N]) > maxi:
        maxi = sum(A[0:i + 1]) + sum(B[i:N])

print(maxi)
