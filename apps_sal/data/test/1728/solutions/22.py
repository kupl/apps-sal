import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\r\n\t "))
n = int(lines[0])
data = lines[1].split(' ')
tree = [0]
for x in data:
    tree.append(int(x))
data = lines[2].split(' ')
colors = [int(data[0])]
operations = 1
for i in range(n):
    if i > 0:
        color = int(data[i])
        parent = tree[i]
        if colors[parent - 1] != color:
            operations += 1
        colors.append(color)
print(operations)
