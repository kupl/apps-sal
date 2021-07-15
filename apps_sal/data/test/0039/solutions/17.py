s = input()
ans = 0
def pal(p):
    return p == p[::-1]
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        if (not pal(s[i:j])):
            ans = max(ans, j - i)
print(ans)

