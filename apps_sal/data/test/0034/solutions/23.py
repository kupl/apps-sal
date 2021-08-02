n, a, b = list(map(int, input().split()))
ans = 0
for x in range(1, min(a, b) + 1):
    k = (a // x) + (b // x)
    if k >= n:
        ans = x
print(ans)
