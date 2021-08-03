d, n = map(int, input().split())

if n == 100:
    ans = (100**d) * (n + 1)
else:
    ans = (100**d) * n
print(ans)
