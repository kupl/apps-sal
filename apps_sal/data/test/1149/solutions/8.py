n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
d = set()
for i in range(1, x[0] + 1):
    d.add(x[i])
for i in range(1, y[0] + 1):
    d.add(y[i])
res = True
for i in range(1, n + 1):
    if not i in d:
        res = False
if res:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
