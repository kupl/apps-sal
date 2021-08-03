def inp():
    return map(int, input().split())


n, k = inp()
a = list(inp())
ans = 0
i = 0
while i != n and a[i] <= k:
    ans += 1
    i += 1
j = n - 1
while i < j and a[j] <= k:
    ans += 1
    j -= 1
print(ans)
