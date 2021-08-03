A, B, N = map(int, input().split())
if N < B:
    ans = int(A * N / B)
else:
    ans = int(A * (B - 1) / B)
print(ans)
