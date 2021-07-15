s = input()
li = []
for i in range(len(s)):
    if i % 2 == 0:
        li.append(s[i])
print((''.join(li)))

