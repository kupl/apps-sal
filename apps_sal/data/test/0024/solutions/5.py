def check(a, x, y):
    left = 0
    right = 0
    for i in range(1, 11):
        if x - i >= 0:
            if a[x - i][y] == 'X':
                left += 1
            else:
                break
        else:
            break
    for i in range(1, 11):
        if x + i < 10:
            if a[x + i][y] == 'X':
                right += 1
            else:
                break
        else:
            break
    if right + left >= 4:
        return 1
    left = 0
    right = 0
    for i in range(1, 11):
        if y - i >= 0:
            if a[x][y - i] == 'X':
                left += 1
            else:
                break
        else:
            break
    for i in range(1, 11):
        if y + i < 10:
            if a[x][y + i] == 'X':
                right += 1
            else:
                break
        else:
            break
    if right + left >= 4:
        return 1
    left = 0
    right = 0
    for i in range(1, 11):
        if x - i >= 0 and y - i >= 0:
            if a[x - i][y - i] == 'X':
                left += 1
            else:
                break
        else:
            break
    for i in range(1, 11):
        if x + i < 10 and y + i < 10:
            if a[x + i][y + i] == 'X':
                right += 1
            else:
                break
        else:
            break
    if right + left >= 4:
        return 1
    left = 0
    right = 0
    for i in range(1, 11):
        if x - i >= 0 and y + i < 10:
            if a[x - i][y + i] == 'X':
                left += 1
            else:
                break
        else:
            break
    for i in range(1, 11):
        if x + i < 10 and y - i >= 0:
            if a[x + i][y - i] == 'X':
                right += 1
            else:
                break
        else:
            break
    if right + left >= 4:
        return 1
    return 0
    
a = []
for i in range(10):
    gg = input()
    a.append([])
    for j in range(10):
        a[i].append(gg[j])
for i in range(10):
    for j in range(10):
        if a[i][j] == '.':
            a[i][j] = 'X'
            if check(a, i, j):
                print("YES")
                return
            a[i][j] = '.'
print("NO")
    

