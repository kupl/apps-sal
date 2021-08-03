a = []
n = int(input())
for i in range(0, n):
    a.append(input())


l = [0 for i in range(0, n)]
c = [0 for i in range(0, n)]


for i in range(0, n):
    for j in range(0, n):
        if a[i][j] == 'E':
            l[i] += 1
            c[j] += 1

if n in l and n in c:
    print('-1')
    return

if n in l:  # am o linie plina de E-uri
    for j in range(0, n):
        i = 0
        while a[i][j] != '.':
            i += 1
        print("%i %i" % (i + 1, j + 1))

else:
    for i in range(0, n):
        j = 0
        while a[i][j] != '.':
            j += 1
        print("%i %i" % (i + 1, j + 1))
