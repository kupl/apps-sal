s = list(input())
g = 0
p = 0
ans = 0
for i in range(len(s)):
    if s[i] == "g":
        if p + 1 <= g:
            ans += 1
            p += 1
        else:
            g += 1
    else:
        if p + 1 <= g:
            p += 1
        else:
            ans -= 1
            g += 1
print(ans)
