r = list(input())
s = ""
count = 0
for i in r:
    if i == "1":
        count = count + 1
    else:
        s = s + i
ans = ""
u = 0
while(u < len(s)):
    if s[u] == "2":
        break
    else:
        u = u + 1
ans = s[:u] + count * "1" + s[u:]
print(ans)
