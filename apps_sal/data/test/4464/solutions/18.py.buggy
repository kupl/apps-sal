import sys
a, b, c = map(int, input().split())
i = 1
l = []
while True:
    aa = a * i % b
    if aa in l:
        break
    l.append(aa)
    i += 1
    if aa != 0 and c % aa == 0:
        print('YES')
        return
print('NO')
