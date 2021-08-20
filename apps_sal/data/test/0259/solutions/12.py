(N, T) = map(int, input().split())
ans = 10 ** 10
Ans = None
for i in range(1, N + 1):
    (a, b) = map(int, input().split())
    if a >= T:
        if a < ans:
            Ans = i
            ans = a
    else:
        k = -(-(T - a) // b)
        if a + k * b < ans:
            Ans = i
            ans = a + k * b
print(Ans)
