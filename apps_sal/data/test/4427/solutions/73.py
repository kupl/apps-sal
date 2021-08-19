(r, d, x) = map(int, input().split())
for i in range(10):
    ans = r * x - d
    print(ans)
    x = ans
