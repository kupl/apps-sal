length = int(input())
string1 = input()
string2 = input()

changes = 0
for i in range(length // 2):
    c1 = string1[i]
    c2 = string1[length - 1 - i]

    c3 = string2[i]
    c4 = string2[length - 1 - i]

    if c1 == c2 and c3 == c4:
        continue
    if c1 == c3 and c2 == c4:
        continue
    if c1 == c4 and c2 == c3:
        continue
    if c3 == c4:
        changes += 1
        continue
    if c1 == c3 or c2 == c4:
        changes += 1
        continue
    if c1 == c4 or c2 == c3:
        changes += 1
        continue
    changes += 2
if length % 2 == 1 and string1[length // 2] != string2[length // 2]:
    changes += 1
print(changes)


