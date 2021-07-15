from sys import stdin

test = stdin.readlines()
n = int(test[0])


dot = 0
j = 0
for i in range(n):
    if test[i+1][j] == '1':
        dot ^= 1
    j += 2

out = []
for q in range(int(test[n + 1])):
    query = test[n + q + 2].split()
    if len(query) == 1:
        out.append(dot)
    else:
        dot ^= 1

print(''.join(map(str, out)))

