import sys
line = sys.stdin.readline().strip().split()
n = int(line[0])
x = int(line[1])
y = int(line[2])
a = list(map(int, sys.stdin.readline().strip().split()))
d = len(a)
s = []
if x > y:
    print(d)
else:
    j = 0
    for i in a:
        if i <= x:
            j = j + 1
    if j % 2 == 0:
        print(j // 2)
    else:
        print(j // 2 + 1)
