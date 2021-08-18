def is_belong(A, C, x, y):
    return A * x + y + C == 0


def solution():
    n = int(input())
    a = [int(i) for i in input().split()]

    other_pointes_indexes = []
    for k in [0, 1]:
        for i in range(1, n):
            if k == i:
                continue
            A = 0
            if k - i != 0:
                A = (a[i] - a[k]) / (k - i)
            C1 = -a[k] - A * k
            C2 = C1

            success = True
            for j in range(n):
                if not is_belong(A, C1, j, a[j]):
                    if C2 != C1:
                        if not is_belong(A, C2, j, a[j]):
                            success = False
                            break
                    else:
                        C2 = -A * j - a[j]
            if success:
                if C1 != C2:
                    print('Yes')
                    return

    print('No')


solution()
