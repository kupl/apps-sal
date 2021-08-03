N, X = map(int, input().split())
m = [int(input()) for _ in range(N)]

gram = X - sum(m)
ans = N + gram // min(m)

print(ans)
