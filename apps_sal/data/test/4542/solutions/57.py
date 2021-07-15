s = input()
ans = 0
p = s[0]
for si in s:
    ans += p != si
    p = si
print(ans)
