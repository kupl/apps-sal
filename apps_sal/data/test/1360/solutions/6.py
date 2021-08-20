n = int(input(''))
cek = []
for i in range(n):
    x = input('')
    temp = []
    temp.extend(list(x.split(' ')))
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    cek.append(temp)
cek.sort()
now = cek[0][1]
for i in range(1, n):
    if cek[i][1] >= now:
        now = cek[i][1]
    else:
        now = cek[i][0]
print(now)
