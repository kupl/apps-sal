N = int(input())
A = [int(a) for a in input().split(" ")]

A.sort(reverse=True)
l1 = 0
c1 = 0
l2 = 0
c2 = 0

L1 = 0
L2 = 0

for i in range(len(A)):
    if L1 and L2:
        break
    elif L1:
        if l2 == A[i]:
            c2 += 1
        elif l2 != A[i]:
            l2 = A[i]
            c2 = 1
        if c2 == 2:
            L2 = l2
    else:
        if l1 == A[i]:
            c1 += 1
        elif l1 != A[i]:
            l1 = A[i]
            c1 = 1
        if c1 == 2:
            L1 = l1

print(L1 * L2)
