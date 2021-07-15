name = input()
line = input()

i_name = 0
i_line = 0

while i_name < len(name) and i_line < len(line):
    if name[i_name] == line[i_line]:
        i_name += 1
    i_line += 1

j_name = len(name) - 1
j_line = len(line) - 1

while j_name >= 0 and j_line >= 0:
    if name[j_name] == line[j_line]:
        j_name -= 1
    j_line -= 1

if i_line <= j_line:
    print(j_line - i_line + 2)
elif i_line - 1 == j_line:
    print(1)
else:
    print(0)

