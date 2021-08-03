N, A, B = map(int, input().split())
ans = A * (N // (A + B)) + min(N % (A + B), A)
print(ans)
