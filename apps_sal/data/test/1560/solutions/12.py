import math
n = int(input())
insects = input()
resr1 = 0
resb1 = 0
for i in range(n):
    if i % 2 == 0 and insects[i] == 'r':
        resr1 += 1
    elif i % 2 == 1 and insects[i] == 'b':
        resb1 += 1
res1 = min(resr1, resb1) + abs(resr1 - resb1)
resr2 = 0
resb2 = 0
for i in range(n):
    if i % 2 == 0 and insects[i] == 'b':
        resb2 += 1
    elif i % 2 == 1 and insects[i] == 'r':
        resr2 += 1
res2 = min(resr2, resb2) + abs(resr2 - resb2)
print(min(res1, res2))
