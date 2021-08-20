s = input()
tmp = 0
length = []
for i in range(len(s)):
    if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or (s[i] == 'T'):
        tmp += 1
        if i == len(s) - 1:
            length.append(tmp)
    else:
        length.append(tmp)
        tmp = 0
print(max(length))
