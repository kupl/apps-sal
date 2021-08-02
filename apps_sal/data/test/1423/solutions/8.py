from operator import itemgetter

n, l, r = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
A = sorted([[a[i], p[i], i, 0] for i in range(n)], key=itemgetter(1))

A[0][3] = l
c = A[0][3] - A[0][0]
for i in range(1, n):
    A[i][3] = max(l, A[i][0] + c + 1)
    c = A[i][3] - A[i][0]
    if A[i][3] > r:
        print(-1)
        break
else:
    A = sorted(A, key=itemgetter(2))
    for i in range(n):
        print(A[i][3], end=" ")
