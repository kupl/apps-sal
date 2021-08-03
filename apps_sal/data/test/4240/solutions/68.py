s = list(input())
t = list(input())

ans = "No"
for i in range(len(s)):
    s0 = s[0]
    s.remove(s0)
    s.append(s0)
    if s == t:
        ans = "Yes"
        break

print(ans)
