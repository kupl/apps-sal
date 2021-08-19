(r, d, ans) = list(map(int, input().split()))
for i in range(10):
    ans = r * ans - d
    print(ans)
