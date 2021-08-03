n = int(input())
s = input()
ans = 0
i = 0
while i < len(s):
    c = s[i]
    j = i + 1
    while j < len(s) and s[i] == s[j]:
        ans += 1
        j += 1
    i = j
print(ans)
