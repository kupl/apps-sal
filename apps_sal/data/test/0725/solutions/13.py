import sys

fin = sys.stdin
fout = sys.stdout
n, m = list(map(int, fin.readline().split()))
a = [0] * n
for i in range(n):
    a[i] = list(fin.readline().split())
for i in range(n):
    for j in range(m):
        if a[i][j] == 'C' or a[i][j] == 'M' or a[i][j] == 'Y':
            fout.write('#Color')
            return
fout.write('#Black&White')

