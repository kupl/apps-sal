s1 = input()
s2 = input()
s1 += s1.upper()
s2 += s2.upper()
d = {}
for i in range(52):
    d[s1[i]] = s2[i]
s = input()
ans = ""
for i in s:
    if not i.isdigit():
        ans += d[i]
    else:
        ans += i
print(ans)
