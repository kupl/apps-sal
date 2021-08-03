import sys
n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
a = sorted(a)
count = 0
c1 = c2 = -1
for i in a:
    if i[0] > c1:
        c1 = i[1]
    elif i[0] > c2:
        c2 = i[1]
    else:
        print('NO')
        return
print('YES')
