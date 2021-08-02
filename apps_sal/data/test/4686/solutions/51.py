w = input()
D = {}
for i in w:
    if i not in D:
        D[i] = 0
    D[i] += 1
for i in D:
    if D[i] % 2 == 1:
        print('No')
        break
else:
    print('Yes')
