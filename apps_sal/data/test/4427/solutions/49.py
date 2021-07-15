r, D, x = map(int, input().split())

ans = x
for _ in range(10):
    ans = r * ans - D
    print(ans)
