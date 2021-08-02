d, n = map(int, input().split())
if n == 100:
    ans = 101 * (100**d)
else:
    ans = 100**d * n
print(ans)
