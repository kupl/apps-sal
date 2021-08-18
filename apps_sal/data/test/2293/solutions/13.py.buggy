m, n = map(int, input().split())
l = []
l = [list(map(int, input().split())) for i in range(m)]

l = [set(i[1:]) for i in l]
for i in range(m):
    for j in range(i + 1, m):
        if len(l[i].intersection(l[j])) == 0:
            print('impossible')
            return
print('possible')
