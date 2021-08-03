N, M = (int(x) for x in input().split())

ans = 2**M * (M * 1900 + (N - M) * 100)
print(ans)
