q = int(input())
for Q in range(q):
    A = [int(i) for i in input().split()]
    A.sort()
    alice = A[0]
    bob = A[1]
    excess = A[2]
    total = sum(A)
    each = total // 2
    print(each)
