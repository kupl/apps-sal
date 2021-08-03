a = list(map(int, input().split()))
s = input().strip()
ans = 0
for i in range(len(s)):
    ans += a[int(s[i]) - 1]
print(ans)
