for _ in range(int(input())):
    x = int(input())
    A = list(map(int, input().split()))
    if A[0] + A[1] > A[-1]:
        print(-1)
    else:
        print(1, 2, x)
