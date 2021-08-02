a = list(map(int, input().split()))
s = input()
ans = 0
for i in range(len(s)):
    ans += a[int(s[i]) - 1]
print(ans)
