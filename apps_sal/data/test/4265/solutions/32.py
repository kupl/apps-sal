s = list(input())
t = list(input())
count = 0
for i in range(len(s)):
    if s[i] == t[i]:
        continue
    elif s[i] != t[i]:
        t[i] = s[i]
        count += 1
print(count)
