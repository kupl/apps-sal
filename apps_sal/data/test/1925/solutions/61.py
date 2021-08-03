A, B, N = list(map(int, input().split()))

ans = 0
if N < B:
    ans = int(A * N / B) - A * int(N / B)
elif N == B:
    ans = int(A * (N - 1) / B) - A * int((N - 1) / B)
else:
    ans = int(A * (B - 1) / B) - A * int((B - 1) / B)
print(ans)
