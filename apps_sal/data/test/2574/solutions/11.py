T = int(input())
while T:
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    a = A[n - 1] * A[n - 2] * A[n - 3] * A[n - 4] * A[n - 5]
    b = A[n - 1] * A[n - 2] * A[n - 3] * A[0] * A[1]
    c = A[n - 1] * A[0] * A[1] * A[2] * A[3]
    print(max(a, b, c))
    T = T - 1
