s = input()
n = len(s)
ans = n
for i in range(n):
    s = s[0:-1]
    ans -= 1
    if s[0:ans // 2] == s[ans // 2:]:
        break
print(ans)
