line = input()
s = ''
k = len(line)
while line[k - 1] != 'e':
    s = line[k - 1] + s
    k = k - 1
line1 = list(line[:k - 1])
b = int(s)
for i in range(0, len(line1)):
    if line1[i] == '.':
        line1.pop(i)
        j = i + b
        if j <= len(line1):
            line1.insert(j, '.')
            u = len(line1) - 1
            dif = 0
            while u > j and line[u] == '0':
                line1.pop()
                u -= 1
        else:
            dif = j - len(line1)
            line1 = line1 + ['0'] * dif
        break
if line1[-1] == '.':
    line1.pop()
print(''.join(y for y in line1))
