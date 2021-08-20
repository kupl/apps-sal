s = input()
t = input()
count = 0
for i in range(0, len(s)):
    if s[i] == t[i]:
        continue
    else:
        count += 1
print(count)
