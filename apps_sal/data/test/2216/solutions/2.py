n,m,k = [int(i) for i in input().split()]
import sys
seq = []
rev = False
for i in range(n):
    l = list(zip([i+1]*m,range(1,m+1)))
    if rev:
        l.reverse()
    seq += l
    rev = not rev

for i in range(k-1):
    sys.stdout.write('2 ' + str(seq[i*2][0]) + ' ' + str(seq[i*2][1]) + ' ' + str(seq[i*2+1][0]) + ' ' + str(seq[i*2+1][1]) + '\n')

print(len(seq) - k*2 + 2,end=' ')
for a,b in seq[k*2-2:]:
    sys.stdout.write(str(a) + ' ' + str(b) + ' ')

