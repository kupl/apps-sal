s = input()

ans = []

x = 0

for i in range(len(s)):
    if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
        x += 1
    else:
        ans.append(x)
        x = 0

ans.append(x)

print((max(ans)))
