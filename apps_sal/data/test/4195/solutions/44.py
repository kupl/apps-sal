(d, n) = list(map(int, input().split()))
ans = 0
if n != 100:
    ans = 100 ** d * n
else:
    ans = 100 ** d * (n + 1)
print(ans)
