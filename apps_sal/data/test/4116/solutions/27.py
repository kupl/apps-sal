n = int(input())
li = []
for i in range(1, 10):
    for j in range(1, 10):
        li.append(i * j)

if n in li:
    print('Yes')
else:
    print('No')
