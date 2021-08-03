t = int(input())

for _ in range(t):
    n = int(input())
    A = [int(x) for x in input().split()]
    for i in range(1, n - 1):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            print('YES')
            print(i, i + 1, i + 2)
            break
    else:
        print('NO')
