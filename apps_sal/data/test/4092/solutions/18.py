n = int(input())
L = [0]
for i in map(int, input().split()):
    L.append(L[-1] + i)
d = dict()
ct = 0
last = 0
for i in L:
    if i not in d:
        d[i] = 1
    else:
        ct += 1
        d = dict()
        d[last] = 1
        d[i] = 1
    last = i
print(ct)
