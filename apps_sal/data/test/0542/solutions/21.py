import sys
numcases = int(sys.stdin.readline())
ht = [0]
at = [0]
x = 2
for casenum in range(1, numcases + 1):
    a = int(sys.stdin.readline())
    if a > 0:
        ht += [a]
        x = 0
    else:
        at += [a * -1]
        x = 1
if sum(ht) != sum(at):
    if sum(ht) > sum(at):
        print('first')
    if sum(ht) < sum(at):
        print('second')
elif ht == at:
    if x == 0:
        print('first')
    else:
        print('second')
elif ht > at:
    print('first')
else:
    print('second')
