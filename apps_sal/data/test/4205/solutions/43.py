N = int(input())
P = [int(s) for s in input().split()]
index = []
for i in range(N):
    index.append(P.index(i + 1))
count = 0
for (i, j) in enumerate(index):
    if i != j:
        count += 1
if count > 2:
    print('NO')
else:
    print('YES')
