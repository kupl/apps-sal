(N, D) = map(int, input().split())
k = 2 * D + 1
print(N // k if N % k == 0 else N // k + 1)
