for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    if A[0] <= A[-1]:
        print('YES')
    else:
        print('NO')
