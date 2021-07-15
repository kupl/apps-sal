__author__ = 'Rakshak.R.Hegde'
n = int(input())
A = list(map(int, input().split()))
A.sort()
m = int(input())
B = list(map(int, input().split()))
B.sort()
pairs = 0
while len(A) and len(B):
    if abs(A[0] - B[0]) <= 1:
        pairs += 1
        del A[0]
        del B[0]
    elif A[0] < B[0]:
        del A[0]
    else:
        del B[0]
print(pairs)
