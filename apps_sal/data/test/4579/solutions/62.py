def __starting_point():
    n = int(input())
    A = []
    for _ in range(n):
        A.append(input())
    A.sort()
    ans = 1
    for i in range(n - 1):
        if A[i] != A[i + 1]:
            ans += 1
    print(ans)


__starting_point()
