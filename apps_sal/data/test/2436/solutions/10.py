for i in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    x = 1
    for j in range(len(A)):
        if 1 + j >= A[j]:
            x = 2 + j
    print(x)
