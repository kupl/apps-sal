(N, X) = map(int, input().split())
m = [int(input()) for i in range(N)]
ans = 0
X -= sum(m)
ans += N
ans += X // min(m)
print(ans)
