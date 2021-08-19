import sys
m = int(sys.stdin.readline())
b = [int(x) for x in sys.stdin.readline().split(' ')]
b.sort()
l1 = []
l2 = []
last = b[0]
rep = 1
l1.append(last)
for i in range(1, len(b)):
    if b[i] == last:
        rep += 1
    else:
        last = b[i]
        rep = 1
    if rep == 1:
        l1.append(last)
    elif rep == 2:
        l2.append(last)
if l2 and l2[-1] == l1[-1]:
    l2.pop()
l2.reverse()
print(len(l1) + len(l2))
print(' '.join([str(x) for x in l1]), end='')
if l2:
    print(' ', end='')
    print(' '.join([str(x) for x in l2]))
else:
    print()
