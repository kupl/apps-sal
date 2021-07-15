n = int(input())
s = list(map(int, input().split()))

ans = 0
for d in range(1, (n-1)//2+1):
    ans_cur = 0
    l, r = 0, n-1
    while r > d and l != r and l != r+d:
        ans_cur += s[l]+s[r]
        ans = max(ans, ans_cur)
        l += d
        r -= d
print(ans)
