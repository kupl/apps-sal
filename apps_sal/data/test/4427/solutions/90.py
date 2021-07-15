r, d, x = (int(i) for i in input().split())
ans = x
for i in range(0, 10):
    ans = r * ans - d
    print(ans)
