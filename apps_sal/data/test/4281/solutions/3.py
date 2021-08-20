import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
A.sort()
B = {A[0] - 1}
C = {A[0] + 1}
for i in range(1, n):
    if A[i] - 1 in B and A[i] in B:
        B.add(A[i] + 1)
    elif A[i] - 1 in B:
        B.add(A[i])
    else:
        B.add(A[i] - 1)
    if A[i] - 1 in C or A[i] in C:
        continue
    else:
        C.add(A[i] + 1)
print(len(C), len(B))
