T = int(input())
for t in range(T):
    n = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    ok = 1
    areas = []
    left = 0

    right = 4 * n - 1
    for i in range(n):
        l1 = left
        l2 = left + 1

        r1 = right
        r2 = right - 1

        if not (A[l1] == A[l2] and A[r1] == A[r2]):
            ok = 0
        areas.append(A[l1] * A[r1])

        left += 2
        right -= 2

    #print(areas, ok)
    if len(set(areas)) == 1 and ok:
        print('YES')
    else:
        print('NO')
