n, q = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
K = [int(i) for i in input().split()]

A = a[:]
for i in range(1, n):
    A[i] += A[i-1]

def bs(A, key):
    lo, hi = 0, len(A)-1
    while lo <= hi:
        mid = (lo+hi) // 2
        if A[mid] == key:
            # print(A)
            # print(f'Found key = {key} *exactly* at mid = {mid}')
            return mid
        elif key < A[mid]:
            hi = mid-1
        elif A[mid] < key:
            lo = mid+1
    # print(A)
    # print(f'hi={hi} > lo={lo}. Returning hi')
    return hi

D = 0
for i in range(q):
    D += K[i]
    # print(f'Accumulated damage = {D}')
    j = bs(A, D)
    if j == n-1:
        # print('Resetting damage')
        D = 0
        j = -1
    print(n-(j+1))

