n, k = map(int, input().split())
x = [*map(int, input().split())]
dad = dict()
a = []
c = 0
for n, i in enumerate(x):
    if dad.get(i, 0) == 0:
        a.append(n + 1)
        c += 1
    if c == k:
        break
    dad[i] = 1
if c < k:
    print('NO')
else:
    print('YES')
    for i in a:
        print(i, end=' ')
