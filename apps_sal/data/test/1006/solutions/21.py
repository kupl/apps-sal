import sys

num_lines = int(input())

lines = []
hash_count = 0

for i in range(num_lines):
    tmp = input()
    lines.append([i for i in tmp])
    hash_count = hash_count + tmp.count("#")

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            try:
                if lines[i + 1][j - 1] == "#" and lines[i + 1][j] == "#" and lines[i + 1][j + 1] == "#" and \
                        lines[i + 2][j] == "#":
                    lines[i + 1][j - 1] = "."
                    lines[i + 1][j] = "."
                    lines[i + 1][j + 1] = "."
                    lines[i + 2][j] = "."
                    hash_count = hash_count - 5
            except:
                print("NO")
                return


if hash_count == 0:
    print("YES")
else:
    print("NO")
