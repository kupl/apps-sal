(N, M) = map(int, input().split())
ans = 1
if abs(N - M) >= 2:
    ans = 0
elif N == M:
    for i in range(1, M + 1):
        ans = ans * i % (10 ** 9 + 7)
    for i in range(1, M + 1):
        ans = ans * i % (10 ** 9 + 7)
    ans = ans * 2 % (10 ** 9 + 7)
else:
    for i in range(1, M + 1):
        ans = ans * i % (10 ** 9 + 7)
    for i in range(1, N + 1):
        ans = ans * i % (10 ** 9 + 7)
print(ans)
