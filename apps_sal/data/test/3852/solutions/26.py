N = int(input())
A = list(map(int, input().split()))
if min(A) >= 0:
    print(N - 1)
    for i in range(1, N):
        print((i, i + 1))
elif max(A) <= 0:
    print(N - 1)
    for i in range(N - 1):
        print((N - i, N - 1 - i))
else:
    (a, b) = (max(A), abs(min(A)))
    print((N - 1) * 2)
    if a >= b:
        d = A.index(a)
        for i in range(N):
            if i != d:
                print((d + 1, i + 1))
        for i in range(1, N):
            print((i, i + 1))
    else:
        d = A.index(-b)
        for i in range(N):
            if i != d:
                print((d + 1, i + 1))
        for i in range(N - 1):
            print((N - i, N - 1 - i))
