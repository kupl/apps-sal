import sys

a = int(sys.stdin.readline().strip())

line = sys.stdin.readline().strip()

to_move = 0

for i in range(a - 1):
    if (line[i] == line[i + 1]):
        to_move += 1

print(to_move)
