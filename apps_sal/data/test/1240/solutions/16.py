import sys
fin = sys.stdin
fout = sys.stdout
results = []
n = int(fin.readline())
columns = [0] * n
allL = 0
allR = 0
for i in range(n):
    (l, r) = list(map(int, fin.readline().split()))
    columns[i] = (l, r)
    allL += l
    allR += r
results.append((abs(allL - allR), -1))
for i in range(n):
    tempL = allL
    tempR = allR
    tempL -= columns[i][0]
    tempR -= columns[i][1]
    tempL += columns[i][1]
    tempR += columns[i][0]
    results.append((abs(tempL - tempR), i))
mR = results[0][0]
mN = results[0][1]
for result in results:
    if result[0] > mR:
        mR = result[0]
        mN = result[1]
fout.write(str(mN + 1))
