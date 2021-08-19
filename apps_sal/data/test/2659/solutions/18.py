def S(i):
    ans = 0
    while i // 10 > 0:
        ans += i % 10
        i //= 10
    ans += i
    return ans


K = int(input())
(Ans, count, N) = ([], 0, 1)
while count < K:
    (N2, Nd) = (N, 1)
    while N2 // 10 > 0:
        Nd += 1
        N2 //= 10
    (minX, X) = (N / S(N), N)
    for i in range(Nd + 2):
        x = (N // 10 ** (i + 1) + 1) * 10 ** (i + 1) - 1
        if minX > x / S(x):
            (minX, X) = (x / S(x), x)
    Ans.append((minX, X))
    count += 1
    N = X + 1
for i in range(K):
    print(Ans[i][1])
