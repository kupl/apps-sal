kuku = []
for i in range(1,10):
    for j in range(1,10):
        if i * j not in kuku:
            kuku.append(i*j)
n = int(input())
if n in kuku:
    print('Yes')
else:
    print('No')
