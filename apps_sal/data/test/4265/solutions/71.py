s = input()
t = input()
count = int(0)
for i in range(len(s)):
    if not s[i] == t[i]:
        count += 1
print(count)
