import sys
fin = sys.stdin
fout = sys.stdout
n = int(fin.readline())
a = list(fin.readline().strip())
b = list(fin.readline().strip())
can1 = [False] * n
b.sort()
for cur in b:
    for i in range(n):
        if cur >= a[i] and (not can1[i]):
            can1[i] = True
            break
fout.write(str(can1.count(False)) + '\n')
a.sort()
can2 = [False] * n
for cur in b:
    for i in range(n):
        if cur > a[i] and (not can2[i]):
            can2[i] = True
            break
fout.write(str(can2.count(True)))
