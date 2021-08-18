
from sys import stdin

stdin.readline()
cnt = 0
acc = 0
for i in map(int, stdin.readline().split()):
    if i == -1:
        if acc > 0:
            acc = acc - 1
        else:
            cnt = cnt + 1
    else:
        acc = acc + i
print(cnt)
