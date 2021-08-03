s = list(input())
m = []
for i in range(0, len(s)):
    if s[i] not in m:
        m.append(s[i])
if len(m) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
