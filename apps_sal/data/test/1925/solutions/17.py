(A, B, N) = map(int, input().split())
if N >= B - 1:
    i = B - 1
    ans = A * i // B - A * (i // B)
else:
    ans = A * N // B - A * (N // B)
print(ans)
