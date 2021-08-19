import sys
my_file = sys.stdin
#my_file = open("input.txt", "r")
line = [int(i) for i in my_file.readline().strip("\n").split()]
r, c = line[0], line[1]
table = my_file.read().split()
new_table = []
for line in table:
    if "S" in line:
        new_table.append(line)
res = (len(table) - len(new_table)) * c
r -= len(table) - len(new_table)
for col in range(c):
    for row in range(r):
        if "S" in new_table[row][col]:
            break
    else:
        res += r
print(res)
