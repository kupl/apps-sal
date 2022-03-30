def is_letter(char):
    return ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('Z')


(n, kk) = map(int, input().split())
placement = [[i for i in input()] for j in range(n)]
kc = 0
for row in placement:
    for i in range(len(row)):
        if row[i] == '.':
            count = 0
            if i > 0 and row[i - 1] == 'S':
                count += 1
            if i < len(row) - 1 and row[i + 1] == 'S':
                count += 1
            row[i] = count
        if row[i] == 'S':
            if i > 0 and is_letter(str(row[i - 1])):
                kc += 1
            if i < len(row) - 1 and is_letter(str(row[i + 1])):
                kc += 1
for i in range(3):
    for j in range(len(placement)):
        if kk == 0:
            break
        for k in range(len(placement[j])):
            if placement[j][k] == i:
                placement[j][k] = 'x'
                kc += i
                kk -= 1
                if kk == 0:
                    break
kkk = 0
for i in range(len(placement)):
    for j in range(len(placement[i])):
        if type(placement[i][j]) == type(1):
            placement[i][j] = '.'
print(kc)
for row in placement:
    print(''.join(row))
