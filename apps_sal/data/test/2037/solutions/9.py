from collections import deque
n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [deque([]) for i in range(n + 1)]
for i in range(m):
    b[a[i]].append(i)
# print(b)
o = False
count = 0
indp = 0
while o == False:
    ind = 0
    for i in range(1, n + 1):
        if len(b[i]) == 0:
            o = True
            break
        ind = max(b[i].popleft(), ind)
    if o == True:
        for i in range(indp, m):
            print(0, end='')
        break
    for i in range(indp, ind):
        print(0, end='')
    indp = ind + 1
    print(1, end='')
print()
