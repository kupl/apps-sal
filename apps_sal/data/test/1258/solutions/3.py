from collections import defaultdict
n = int(input())
A = []
for i in range(n - 2):
    A.append(list(map(int, input().split())))
count = {i + 1: 0 for i in range(n)}
third = {}
for (a, b, c) in A:
    if (a, b) not in third:
        third[a, b] = []
    third[a, b].append(c)
    if (b, a) not in third:
        third[b, a] = []
    third[b, a].append(c)
    if (a, c) not in third:
        third[a, c] = []
    third[a, c].append(b)
    if (c, a) not in third:
        third[c, a] = []
    third[c, a].append(b)
    if (b, c) not in third:
        third[b, c] = []
    third[b, c].append(a)
    if (c, b) not in third:
        third[c, b] = []
    third[c, b].append(a)
    count[a] += 1
    count[b] += 1
    count[c] += 1
first = 0
for i in range(n):
    if count[i + 1] == 1:
        first = i + 1
        break
second = 0
for i in range(n):
    if count[i + 1] == 2:
        second = i + 1
        if (first, second) in third:
            break
        else:
            second = 0
ans = [first, second]
aset = set()
aset.add(first)
aset.add(second)
for i in range(n - 2):
    for val in third[first, second]:
        if val not in aset:
            ans.append(val)
            aset.add(val)
            (first, second) = (second, val)
            break
print(*ans)
