import sys

fin = sys.stdin
fout = sys.stdout
n = int(fin.readline())
m = ['a', 'b']
s = ''
for i in range(n):
    s += m[(i // 2) % 2]
fout.write(s)
