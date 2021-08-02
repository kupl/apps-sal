
s = input()
ans = 0
n = len(s)
for i in range(n):
    t = ""
    for j in range(i, n):
        t += s[j]
        if(t != t[::-1]):
            ans = max(ans, len(t))
print(ans)
