s = input()
sr = s[::-1]

for i in range(len(s)):
    if s[i] == "A":
        st = i + 1
        break

for i in range(len(s)):
    if sr[i] == "Z":
        en = len(s) - i
        break

print(en - st + 1)
