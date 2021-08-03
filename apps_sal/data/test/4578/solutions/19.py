n, x = map(int, input().split())
m = [int(input()) for _ in range(n)]
ans = (x - sum(m)) // min(m)
print(n + ans)
