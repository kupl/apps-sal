MOD = 10 ** 9 + 7
(N, X, T) = list(map(int, input().split()))
ans = T * (N // X + (N % X != 0))
print(ans)
