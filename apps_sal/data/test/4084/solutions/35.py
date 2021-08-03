N, A, B = map(int, input().split())

C = A + B

ans = A * (N // C)
ans += min(N % C, A)

print(ans)
