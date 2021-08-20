def check(s, t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        i += 1
    return j == len(t)


s = input()
t = input()
ans = 0
for i in range(len(s) + 1):
    for j in range(i, len(s) + 1):
        if check(s[:i] + s[j:], t):
            ans = max(ans, j - i)
print(ans)
