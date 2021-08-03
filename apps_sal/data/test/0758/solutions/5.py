n = int(input())
s = input().strip()
ans = 0
for i in range(len(s)):
    if s[i] == "B":
        ans += 2 ** i
print(ans)
