import sys
a = list(input())
n = int(input())
if len(a) < n:
    print('impossible')
    return
b = {}
c = 0
for i in a:
    if i in list(b.keys()):
        b[i] += 1
        c += 1
    else:
        b[i] = 1
if len(list(b.keys())) >= n:
    print(0)
elif n - len(list(b.keys())) <= c:
    print(n - len(list(b.keys())))
else:
    print('impossible')
