a = []

for i in range(4):
    a.append(input())

for i in range(3):
    for j in range(3):
        k = 0
        if a[i][j] == '#':
            k += 1
        if a[i][j+1] == '#':
            k += 1
        if a[i+1][j] == '#':
            k += 1
        if a[i+1][j+1] == '#':
            k += 1
        if k>=3:
            print("YES")
            return
        k = 0
        if a[i][j] == '.':
            k += 1
        if a[i][j+1] == '.':
            k += 1
        if a[i+1][j] == '.':
            k += 1
        if a[i+1][j+1] == '.':
            k += 1
        if k>=3:
            print("YES")
            return
print("NO")





