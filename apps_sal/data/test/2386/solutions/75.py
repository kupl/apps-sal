def resolve():
    inf = 10 ** 10 + 1
    N = int(input())
    A = [int(x) for x in input().split(' ')]
    for i in range(N):
        A[i] -= i + 1
    A.sort()
    if len(A) % 2:
        b = A[len(A) // 2]
    else:
        b = round((A[len(A) // 2] + A[len(A) // 2 - 1]) // 2)
    ans = 0
    for i in range(N):
        ans += abs(A[i] - b)
    print(ans)


resolve()
