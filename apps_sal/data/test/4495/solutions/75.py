(a, b, x) = map(int, input().split())
res1 = (a - 1) // x
res2 = b // x
ans = res2 - res1
print(ans)
