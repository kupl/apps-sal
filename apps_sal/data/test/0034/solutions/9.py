n, a, b = list(map(int, input().split()))
ans = 0
for x in range(1, n):
    # if a//x>0 and b//(n-x)>0:
    ans = max(ans, min(a // x, b // (n - x)))
print(ans)
