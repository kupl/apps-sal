N, M = map(int, input().rstrip().split(" "))
if abs(N - M) > 1:
    print(0)
else:
    ans = 1
    for i in range(1, N + 1):
        ans *= i
        ans %= 10 ** 9 + 7
    for i in range(1, M + 1):
        ans *= i
        ans %= 10 ** 9 + 7
    if N == M:
        ans *= 2
        ans %= 10 ** 9 + 7
    print(ans)
