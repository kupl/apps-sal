from copy import copy
N = int(input())
A = list(map(int,(input().split())))

A.insert(0,-10000000)
B = copy(A)
ans = []
bns = []

for i in range(1,N):
    if A[i] > A[i+1]:
        if A[i] >= 0 and A[i+1] >= 0:
            A[i+1] += A[i]
            ans.append([i,i+1])
        elif A[i] <= 0 and A[i+1] <= 0:
            A[i] += A[i+1]
            ans.append([i+1,i])
        else:
            if abs(A[i]) <= abs(A[i+1]):
                A[i] += A[i+1]
                ans.append([i+1,i])
                A[i] += A[i+1]
                ans.append([i+1,i])
            else:
                A[i+1] += A[i]
                ans.append([i,i+1])
                A[i+1] += A[i]
                ans.append([i,i+1])
for i in range(1,N)[::-1]:
    if A[i] > A[i+1]:
        if A[i] >= 0 and A[i+1] >= 0:
            A[i+1] += A[i]
            ans.append([i,i+1])
        elif A[i] <= 0 and A[i+1] <= 0:
            A[i] += A[i+1]
            ans.append([i+1,i])
        else:
            if abs(A[i]) <= abs(A[i+1]):
                A[i] += A[i+1]
                ans.append([i+1,i])
                A[i] += A[i+1]
                ans.append([i+1,i])
            else:
                A[i+1] += A[i]
                ans.append([i,i+1])
                A[i+1] += A[i]
                ans.append([i,i+1])

A = B
for i in range(1,N)[::-1]:
    if A[i] > A[i+1]:
        if A[i] >= 0 and A[i+1] >= 0:
            A[i+1] += A[i]
            bns.append([i,i+1])
        elif A[i] <= 0 and A[i+1] <= 0:
            A[i] += A[i+1]
            bns.append([i+1,i])
        else:
            if abs(A[i]) <= abs(A[i+1]):
                A[i] += A[i+1]
                bns.append([i+1,i])
                A[i] += A[i+1]
                bns.append([i+1,i])
            else:
                A[i+1] += A[i]
                bns.append([i,i+1])
                A[i+1] += A[i]
                bns.append([i,i+1])
for i in range(1,N):
    if A[i] > A[i+1]:
        if A[i] >= 0 and A[i+1] >= 0:
            A[i+1] += A[i]
            bns.append([i,i+1])
        elif A[i] <= 0 and A[i+1] <= 0:
            A[i] += A[i+1]
            bns.append([i+1,i])
        else:
            if abs(A[i]) <= abs(A[i+1]):
                A[i] += A[i+1]
                bns.append([i+1,i])
                A[i] += A[i+1]
                bns.append([i+1,i])
            else:
                A[i+1] += A[i]
                bns.append([i,i+1])
                A[i+1] += A[i]
                bns.append([i,i+1])

M = len(ans)
L = len(bns)
if M <= L:
    print(M)
    for i in range(M):
        print(*ans[i])
else:
    print(L)
    for i in range(L):
        print(*bns[i])
