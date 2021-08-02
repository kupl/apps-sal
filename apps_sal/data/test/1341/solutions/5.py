line = input()
commands = input()

current = line[0]
j = 0
for i in commands:
    if i == line[j]:
        j += 1

print(j + 1)
