a = [''] * 2
b = [''] * 2
for i in range(2):
    a[i] = input()
for i in range(2):
    b[i] = input()
way1 = ''
way2 = ''
for i in range(2):
    if i == 0:
        for q in range(2):
            if a[i][q] != 'X':
                way1 += a[i][q]
            if b[i][q] != 'X':
                way2 += b[i][q]
    else:
        for q in range(1, -1, -1):
            if a[i][q] != 'X':
                way1 += a[i][q]
            if b[i][q] != 'X':
                way2 += b[i][q]
for i in range(3):
    if way1 == way2:
        print("YES")
        return
    way2 = way2[1:] + way2[0]
print("NO")
return
