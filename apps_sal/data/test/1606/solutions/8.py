from sys import stdin

n = int(stdin.readline())
dot = 0
j = 0
for i in range(0, 2 * n, 2):
    line = stdin.readline()
    if line[i] == '1':
        dot ^= 1

out = []
stdin.readline()
for query in stdin:
    if len(query) < 3:
        out.append('1' if dot else '0')
    else:
        dot ^= 1

print(''.join(out))

