female = "CHAT WITH HER!"
male = "IGNORE HIM!"
name = input()
uniqueChar = []
for i in name:
    if not i in uniqueChar:
        uniqueChar.append(i)

if len(uniqueChar) % 2 == 0:
    print(end=female)
else:
    print(end=male)
