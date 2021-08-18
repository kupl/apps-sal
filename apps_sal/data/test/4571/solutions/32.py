N, M = list(map(int, input().split()))
A = 1900 * M + 100 * (N - M)

ans = A * pow(2, M)
print(ans)
