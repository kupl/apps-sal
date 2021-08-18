for _ in range(int(input())):
    A = []
    C = []
    n, m = list(map(int, input().split()))
    for i in range(n):
        B = list(map(int, input().split()))
        A.append(B)
    for i in range((n + m - 1)):
        C.append([])
        for j in range(i + 1):
            if (i - j) < n and j < m:
                C[-1].append(A[i - j][j])
    Ans = 0
    for i in range(len(C) // 2):
        Ans += min(sum(C[i]) + sum(C[- i - 1]), len(C[i]) + len(C[-1 - i]) - sum(C[i]) - sum(C[- i - 1]))
    print(Ans)
