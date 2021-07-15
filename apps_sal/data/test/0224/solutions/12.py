s = input()
a = "AEUYEOI"
pos = [0]
for i in range(len(s)):
    if s[i] in a:
        pos.append(i + 1)
pos.append(len(s) + 1)
max_ = pos[1] - pos[0]
for i in range(2, len(pos)):
    max_ = max(max_, pos[i] - pos[i - 1])
print(max_)
