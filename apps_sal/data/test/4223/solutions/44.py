n = int(input())
s = input()
ans = 0
i = 0
while i < n:
    ans += 1
    while i + 1 < n and s[i] == s[i + 1]:
        i += 1
    i += 1
print(ans)
