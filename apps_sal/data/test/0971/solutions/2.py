import sys

fin = sys.stdin
fout = sys.stdout
n, b, d = list(map(int, fin.readline().split()))
a = list(map(int, fin.readline().split()))
summ = 0
count = 0
for cur in a:
    if cur > b:
        continue
    summ += cur
    if summ > d:
        count += 1
        summ = 0
fout.write(str(count))

