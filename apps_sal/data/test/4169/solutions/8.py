def resolve():
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        a = list(map(int, input().split()))
        A.append(a)
    ans = 0
    for i, j in sorted(A, key=lambda x: x[0]):
        if j >= M:
            ans += M * i
            print(ans)
            return
        ans += i * j
        M -= j


resolve()
