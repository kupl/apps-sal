N = int(input())
l = []
for i in range(1, 10):
    for j in range(i, 10):
        l.append(i * j)
if N in l:
    print('Yes')
else:
    print('No')
