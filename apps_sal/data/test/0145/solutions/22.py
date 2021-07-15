names = input()

letters = []
for i in range(0, len(names)):
    if letters.count(names[i]) == 0:
        letters.append(names[i])

if len(letters) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

