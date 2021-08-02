n = int(input())
d = {1: []}
for i in range(n - 1):
    parent = int(input())
    if parent in d:
        d[parent].append(i + 2)
    else:
        d[parent] = [i + 2]
for i in d:
    count = 0
    for j in d[i]:
        if j not in d:
            count += 1
    if count < 3:
        print('No')
        return
print('Yes')
