N = int(input())
A = [int(a) for a in input().split(' ')]
B = [int(b) for b in input().split(' ')]
C = [int(c) for c in input().split(' ')]
A.sort()
B.sort()
C.sort()
combiBC = [0] * len(B)
ic = 0
lc = len(C)
for ib in range(len(B)):
    b = B[ib]
    while ic < lc:
        c = C[ic]
        if b >= c:
            ic += 1
        else:
            combiBC[ib] = lc - ic
            break
sumCombiBC = []
for i in range(len(combiBC)):
    if i == 0:
        sumCombiBC.append(combiBC[-1])
    else:
        sumCombiBC.insert(0, combiBC[-i - 1] + sumCombiBC[0])
cnt = 0
ib = 0
for ia in range(len(A)):
    a = A[ia]
    while ib < len(B):
        b = B[ib]
        if a >= b:
            ib += 1
        else:
            cnt += sumCombiBC[ib]
            break
print(cnt)
