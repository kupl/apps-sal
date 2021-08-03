n = int(input())
s = list(map(int, input().split()))
ans = 0
for i in range(1, (n - 1) // 2 + 1):
    res = 0
    l, r = i, n - 1 - i
    while r > i and l != r and l != r + i:
        res += s[l] + s[r]
        ans = max(ans, res)
        l += i
        r -= i
print(ans)
