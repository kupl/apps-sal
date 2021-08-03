s = input()
li = []
for i in range(1, len(s) - 1):
    if int(s[i - 1:i + 2]) >= 753:
        li.append(int(s[i - 1:i + 2]) - 753)
    else:
        li.append((753 - int(s[i - 1:i + 2])))

print(min(li))
