N, M = map(int, input().split())
A = 1900 * M + 100 * (N - M)

ans = A * 2**M

print(ans)
