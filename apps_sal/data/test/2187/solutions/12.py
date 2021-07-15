for _ in range(int(input())):
    x = int(input())
    Ans = 0
    A = list(map(int, input().split()))
    for i in range(x - 1):
        if A[i] > A[i + 1]:
            Ans += A[i] - A[i + 1]
    print(Ans)
