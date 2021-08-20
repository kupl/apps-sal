N = int(input())
A = []
for i in range(1, 10):
    for j in range(1, 10):
        A.append(i * j)
if N in A:
    print('Yes')
else:
    print('No')
