a = input().split()
n, k = int(a[0]), int(a[1])
zero = []
one = []
two = []
plain = []
neighbours = 0
notS = ['P', '-', '.']
for i in range(n):
    row = input()
    plain.append(list(row))
    for e in range(len(row)):
        if row[e] == '.':
            if e == 0:
                if row[e + 1] in notS:
                    zero.append((i, e))
                elif row[e + 1] == 'S':
                    one.append((i, e))
            else:
                if e != len(row) - 1:
                    if row[e + 1] in notS and row[e - 1] in notS:
                        zero.append((i, e))
                    elif (row[e + 1] in notS and row[e - 1] not in notS) or (row[e - 1] in notS and row[e + 1] not in notS):
                        one.append((i, e))
                    else:
                        two.append((i, e))
                else:
                    if row[e - 1] in notS:
                        zero.append((i, e))
                    else:
                        one.append((i, e))
        elif row[e] == 'P':
            if e == 0:
                if row[e + 1] == 'S':
                    neighbours += 1
            else:
                if e == len(row) - 1:
                    if row[e - 1] == 'S':
                        neighbours += 1
                else:
                    if row[e - 1] == 'S':
                        neighbours += 1
                    if row[e + 1] == 'S':
                        neighbours += 1
        elif row[e] == 'S':
            if e == 0:
                if row[e + 1] == 'S':
                    neighbours += 1
            else:
                if e == len(row) - 1:
                    if row[e - 1] == 'S':
                        neighbours += 1
                else:
                    if row[e - 1] == 'S':
                        neighbours += 1
                    if row[e + 1] == 'S':
                        neighbours += 1
for i in range(len(zero)):
    if k != 0:
        k -= 1
        plain[zero[i][0]][zero[i][1]] = 'x'
    else:
        break
if k != 0:
    for i in range(len(one)):
        if k != 0:
            k -= 1
            plain[one[i][0]][one[i][1]] = 'x'
            neighbours += 1
        else:
            break
    if k != 0:
        for i in range(len(two)):
            if k != 0:
                k -= 1
                plain[two[i][0]][two[i][1]] = 'x'
                neighbours += 2
            else:
                break
print(neighbours)
for i in range(n):
    print(''.join(plain[i]))







