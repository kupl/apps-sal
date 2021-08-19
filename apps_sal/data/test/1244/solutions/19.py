n = int(input())
c = {}
for x in (int(x) for x in input().split()):
    c[x] = 1 if x not in c else c[x] + 1
val = sum((1 for x in c if c[x] > (n + 1) // 2))
print('NO' if val else 'YES')
