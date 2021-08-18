

n = int(input())

mas = []
all_h = 0
for i in range(n):
    line = input()
    s = line.count('s')
    h = line.count('h')
    all_h += h

    if h == 0:
        k = 100000
    else:
        k = s / h
    mas.append((k, line))


sor = sorted(mas, key=lambda val: val[0], reverse=True)
str = ''

for item in sor:
    str += item[1]


count = 0
count_h = all_h
for i in range(len(str)):
    if str[i] == 'h':
        count_h -= 1

    else:
        count += count_h


print(count)
