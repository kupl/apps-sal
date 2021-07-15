import sys

n = int(input())
m = sorted(list(set(map(int, input().split()))))

f = False
for i in range(len(m)-2):
    if m[i+1]-m[i] <= 2 and m[i+2]-m[i+1] <= 2 and m[i+2]-m[i] <= 2:
        print('YES')
        f = True
        break

if not f:
    print('NO')
