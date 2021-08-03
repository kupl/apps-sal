s = input()
t = input()
ans = 0
for i in range(len(t)):
    if s[i] != t[i]:
        ans += 1
print(ans)
