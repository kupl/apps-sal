s = input().strip()
ans = 0
last = 2
for i in range(3, len(s)):
    if s[i - 3: i + 1] == "bear":
        last = i
    ans += last - 2
print(ans)

