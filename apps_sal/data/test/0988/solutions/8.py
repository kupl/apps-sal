txt = []
a = ''
for i in range(6):
    a = input()
    txt.append(a)

b = [[3, 3, 0, 4, 4, 0, 3, 3], [3, 3, 0, 4, 4, 0, 3, 3], [2, 2, 0, 3, 3, 0, 2, 2], [2, 2, 0, 3, 3, 0, 2, 2], [1, 1, 0, 2, 2, 0, 1, 1], [1, 1, 0, 2, 2, 0, 1, 1]]

max = 0
maxi = 0
maxj = 0
for i in range(6):
    for j in range(8):
        if (txt[i][j] == '.'):
            if(b[i][j] > max):
                max = b[i][j]
                maxi = i
                maxj = j

for i in range(6):
    if (i == maxi):
        print(txt[i][:maxj] + 'P' + txt[i][maxj + 1:])
        continue
    print(txt[i])
