n, x = map(int,input().split())
L = list(int(input()) for _ in range(n))
m = min(L)
tmp = x - sum(L)
ans = n
ans += tmp//m
print(ans)
