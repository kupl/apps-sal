import sys

n,m = input().split(' ')
dos = input().split(' ')
current = 1
result = 0
circle = list(range(1,int(n)))
for do in dos:
    tmp = int(do) - current
    if tmp < 0:
        result += int(n) + tmp
    else:
        result += tmp
    current = int(do)
print(result)

