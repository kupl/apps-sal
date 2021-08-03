N = int(input())
A = sorted(list(set([int(a) for a in input().split()])))
if len(A) == 1:
    print(0)
elif len(A) == 2:
    if (A[1] - A[0]) % 2 == 0:
        print((A[1] - A[0]) // 2)
    else:
        print(A[1] - A[0])
elif len(A) == 3:
    if A[2] + A[0] == A[1] * 2:
        print(A[2] - A[1])
    else:
        print(-1)
else:
    print(-1)
