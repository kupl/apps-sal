ans = 0
s = input()
n = len(s)
for i in range(n):
    for j in range(i + 1, n + 1):
        t = s[i:j]
        if t != t[::-1]:
            ans = max(ans, j - i)
print(ans)
