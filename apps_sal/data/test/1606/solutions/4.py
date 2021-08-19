from sys import stdin
test = stdin.readlines()
n = int(test[0])
matrix = [test[i + 1].split() for i in range(n)]
dot = 0
for i in range(n):
    dot ^= matrix[i][i] == '1'
out = []
for q in range(int(test[n + 1])):
    query = test[n + q + 2].split()
    if len(query) == 1:
        out.append(dot)
    else:
        dot ^= 1
print(''.join(map(str, out)))
