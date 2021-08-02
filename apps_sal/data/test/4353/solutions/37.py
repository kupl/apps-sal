s = input()

S = ""
for i in range(len(s)):
    if s[i] == ',':
        S += " "
    else:
        S += s[i]

print(S)
