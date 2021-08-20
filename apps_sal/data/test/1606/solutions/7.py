from sys import stdin
n = int(stdin.readline())
dot = 0
j = 0
for i in range(n):
    line = stdin.readline()
    if line[j] == '1':
        dot ^= 1
    j += 2
out = []
stdin.readline()
for query in stdin:
    if len(query) < 3:
        out.append('1' if dot else '0')
    else:
        dot ^= 1
print(''.join(out))
