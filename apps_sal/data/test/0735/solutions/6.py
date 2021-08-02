
n = int(input())
A = list(map(int, input().split()))
sA = sorted(A)

pa = 1
while pa <= n and A[pa - 1] == sA[pa - 1]:
    pa = pa + 1

if pa == n + 1:
    print('yes\n1 1')
else:
    pb = n
    while pb >= 1 and A[pb - 1] == sA[pb - 1]:
        pb = pb - 1

    AB = A[pa - 1:pb]
    rAB = reversed(AB)
    sAB = sA[pa - 1:pb]
    can = sum(1 for (x, y) in zip(sAB, rAB) if x != y)
    if can == 0:
        print('yes')
        print(pa, pb)
    else:
        print('no')
